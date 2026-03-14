# Stage 1: Get FalkorDB module from official image
FROM falkordb/falkordb:latest AS falkordb-source

# Stage 2: Build the application
FROM python:3.11-slim-bookworm

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    redis-server \
    redis-tools \
    && rm -rf /var/lib/apt/lists/*

# Copy FalkorDB module from official image
COPY --from=falkordb-source /FalkorDB/bin/linux-x64-release/src/falkordb.so /opt/falkordb.so
RUN chmod 755 /opt/falkordb.so

WORKDIR /app

# Python dependencies
RUN pip install --no-cache-dir \
    falkordb>=1.0.0 \
    numpy>=1.24.0 \
    httpx>=0.24.0 \
    pydantic>=2.0.0 \
    pyyaml>=6.0 \
    fastapi>=0.100.0 \
    uvicorn>=0.30.0 \
    python-dotenv>=1.0.0

# Application code
COPY . /app/

# Startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Persistent data + logs directories
RUN mkdir -p /data/falkordb /data/state /app/logs

EXPOSE 8080

CMD ["/start.sh"]
