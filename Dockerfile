# Estágio 1: Builder
FROM python:3.11-slim AS builder

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./
COPY src/ ./src/

RUN poetry build


# Estágio 2: Runtime
FROM python:3.11-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

COPY --from=builder /app/dist/*.whl /app/

RUN pip install --no-cache-dir /app/*.whl && rm -f /app/*.whl

USER appuser

ENTRYPOINT ["cyp2d6-classifier"]
CMD ["--help"]
