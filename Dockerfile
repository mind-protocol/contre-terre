FROM python:3.11-slim-bookworm

# System dependencies: redis-server (for FalkorDB), curl, wget
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    redis-server \
    redis-tools \
    curl \
    ca-certificates \
    wget \
    && rm -rf /var/lib/apt/lists/*

# FalkorDB module: download the .so for redis-server --loadmodule
ARG FALKORDB_VERSION=v4.16.7
RUN wget -q "https://github.com/FalkorDB/FalkorDB/releases/download/${FALKORDB_VERSION}/falkordb-x64.so" \
    -O /opt/falkordb.so \
    && chmod 755 /opt/falkordb.so

WORKDIR /app

# Python dependencies (mind runtime + embeddings)
RUN pip install --no-cache-dir \
    falkordb>=1.0.0 \
    numpy>=1.24.0 \
    httpx>=0.24.0 \
    pydantic>=2.0.0 \
    pyyaml>=6.0 \
    fastapi>=0.100.0 \
    uvicorn>=0.30.0 \
    python-dotenv>=1.0.0 \
    sentence-transformers>=2.2.0

# Application code
COPY . /app/

# Startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Persistent data + logs directories
RUN mkdir -p /data/falkordb /data/state /app/logs

EXPOSE 8080

CMD ["/start.sh"]
