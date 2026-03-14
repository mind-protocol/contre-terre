# Use the official FalkorDB image as base — it already has redis + the module
FROM falkordb/falkordb:latest

# Install Python 3 on top
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python dependencies (minimal — no sentence-transformers)
RUN pip3 install --no-cache-dir --break-system-packages \
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

EXPOSE 10000

# Override FalkorDB's entrypoint — we manage redis ourselves in start.sh
ENTRYPOINT []
CMD ["/start.sh"]
