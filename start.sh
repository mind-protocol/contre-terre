#!/bin/bash
set -e

echo "[start] Contre-Terre deployment starting..."

DATA_DIR="/data"
APP_DIR="/app"

# ── 1. Ensure persistent directories exist ────────────────────────────────
mkdir -p "$DATA_DIR/falkordb" "$DATA_DIR/state" "$APP_DIR/logs"

# ── 2. Generate .env from Render environment variables ────────────────────
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

# ── 3. Start FalkorDB (redis-server + module) ────────────────────────────
echo "[start] Starting FalkorDB..."
redis-server \
    --loadmodule /opt/falkordb.so \
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

# ── 4. Wait for FalkorDB to be ready ─────────────────────────────────────
echo "[start] Waiting for FalkorDB..."
for i in $(seq 1 30); do
    if redis-cli -h 127.0.0.1 -p 6379 ping 2>/dev/null | grep -q PONG; then
        echo "[start] FalkorDB ready (attempt $i)"
        break
    fi
    if [ "$i" -eq 30 ]; then
        echo "[start] ERROR: FalkorDB failed to start after 30 attempts"
        cat "$APP_DIR/logs/falkordb.log" 2>/dev/null || true
        exit 1
    fi
    sleep 1
done

# Verify FalkorDB module loaded
MODULE_CHECK=$(redis-cli -h 127.0.0.1 -p 6379 MODULE LIST 2>/dev/null || true)
if echo "$MODULE_CHECK" | grep -qi "graph"; then
    echo "[start] FalkorDB module loaded successfully"
else
    echo "[start] WARNING: FalkorDB module may not be loaded"
    echo "$MODULE_CHECK"
fi

# ── 5. Set environment for MCP server ─────────────────────────────────────
export PYTHONPATH="$APP_DIR/.mind/runtime:$APP_DIR"
export PYTHONUNBUFFERED=1
export FALKORDB_HOST="${FALKORDB_HOST:-localhost}"
export FALKORDB_PORT="${FALKORDB_PORT:-6379}"
export FALKORDB_GRAPH="${FALKORDB_GRAPH:-contre_terre}"
export DATABASE_BACKEND="${DATABASE_BACKEND:-falkordb}"
export PORT="${PORT:-8080}"

# ── 6. Start the HTTP server ─────────────────────────────────────────────
echo "[start] Starting Contre-Terre server on port $PORT..."
exec python3 -m uvicorn server:app --host 0.0.0.0 --port "$PORT" --log-level info
