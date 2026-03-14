FROM python:3.11-slim-bookworm

WORKDIR /app

RUN pip install --no-cache-dir \
    fastapi>=0.100.0 \
    uvicorn>=0.30.0 \
    pydantic>=2.0.0 \
    pyyaml>=6.0 \
    python-dotenv>=1.0.0

COPY data/seed/ /app/data/seed/
COPY data/brains/ /app/data/brains/
COPY data/citizens.json /app/data/citizens.json
COPY world-manifest.json /app/world-manifest.json
COPY server.py /app/server.py
COPY seed_contre_terre_graph.py /app/seed_contre_terre_graph.py

EXPOSE 10000

CMD ["python3", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "10000"]
