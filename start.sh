#!/bin/bash
set -e

echo "[start] Contre-Terre deployment starting..."

DATA_DIR="/data"
APP_DIR="/app"

# ── 1. Ensure persistent directories exist
mkdir -p "$DATA_DIR/falkordb" "$DATA_DIR/state" "$APP_DIR/logs"

# ── 2. Generate .env from Render environment variables
ENV_FILE="$APP_DIR/.env"
echo "# Auto-generated at $(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$ENV_FILE"
for var in DATABASE_BACKEND FALKORDB_HOST FALKORDB_PORT FALKORDB_GRAPH \
    EMBEDDING_PROVIDER OPENAI_API_KEY OPENAI_EMBEDDING_MODEL \
    ANTHROPIC_API_KEY RENDER; do
    val=$(printenv "$var" 2>/dev/null || true)
    if [ -n "$val" ]; then
        echo "${var}=${val}" >> "$ENV_FILE"
    fi
done
echo "[start] Generated .env with $(grep -c '=' "$ENV_FILE") vars"

# ── 3. Find redis-server and FalkorDB module
REDIS_SERVER=""
for rs in /var/lib/falkordb/bin/redis-server /usr/bin/redis-server /usr/local/bin/redis-server; do
    if [ -x "$rs" ]; then REDIS_SERVER="$rs"; break; fi
done
if [ -z "$REDIS_SERVER" ]; then
    REDIS_SERVER=$(which redis-server 2>/dev/null || true)
fi
echo "[start] redis-server: ${REDIS_SERVER:-NOT FOUND}"

FALKORDB_SO=""
for path in /var/lib/falkordb/bin/falkordb.so /FalkorDB/bin/linux-x64-release/src/falkordb.so /opt/falkordb.so /usr/lib/redis/modules/falkordb.so; do
    if [ -f "$path" ]; then FALKORDB_SO="$path"; break; fi
done
echo "[start] falkordb.so: ${FALKORDB_SO:-NOT FOUND}"

if [ -z "$REDIS_SERVER" ] || [ -z "$FALKORDB_SO" ]; then
    echo "[start] Searching filesystem..."
    find / -name "redis-server" -type f 2>/dev/null | head -3
    find / -name "falkordb.so" -type f 2>/dev/null | head -3
    echo "[start] WARNING: Starting server without FalkorDB"
fi

# ── 4. Start FalkorDB if found
if [ -n "$REDIS_SERVER" ] && [ -n "$FALKORDB_SO" ]; then
    echo "[start] Starting FalkorDB..."
    "$REDIS_SERVER" \
        --loadmodule "$FALKORDB_SO" \
        --port 6379 \
        --bind 127.0.0.1 \
        --dir "$DATA_DIR/falkordb" \
        --dbfilename dump.rdb \
        --save 60 1 \
        --save 300 10 \
        --appendonly yes \
        --appendfilename appendonly.aof \
        --maxmemory 256mb \
        --maxmemory-policy noeviction \
        --protected-mode yes \
        --daemonize yes \
        --logfile "$APP_DIR/logs/falkordb.log"

    # ── 5. Wait for FalkorDB to be ready
    echo "[start] Waiting for FalkorDB..."
    REDIS_CLI=""
    for rc in /var/lib/falkordb/bin/redis-cli /usr/bin/redis-cli /usr/local/bin/redis-cli; do
        if [ -x "$rc" ]; then REDIS_CLI="$rc"; break; fi
    done
    REDIS_CLI="${REDIS_CLI:-$(which redis-cli 2>/dev/null || echo redis-cli)}"

    for i in $(seq 1 30); do
        if "$REDIS_CLI" -h 127.0.0.1 -p 6379 ping 2>/dev/null | grep -q PONG; then
            echo "[start] FalkorDB ready (attempt $i)"
            break
        fi
        if [ "$i" -eq 30 ]; then
            echo "[start] ERROR: FalkorDB failed to start"
            cat "$APP_DIR/logs/falkordb.log" 2>/dev/null || true
        fi
        sleep 1
    done
else
    echo "[start] Skipping FalkorDB start — binaries not found"
fi

# ── 6. Set environment
export PYTHONPATH="$APP_DIR"
export PYTHONUNBUFFERED=1
export FALKORDB_HOST="${FALKORDB_HOST:-localhost}"
export FALKORDB_PORT="${FALKORDB_PORT:-6379}"
export FALKORDB_GRAPH="${FALKORDB_GRAPH:-contre_terre}"
export PORT="${PORT:-10000}"

# ── 7. Start the HTTP server
echo "[start] Starting Contre-Terre server on port $PORT..."
exec python3 -m uvicorn server:app --host 0.0.0.0 --port "$PORT" --log-level info
