FROM node:22-bookworm-slim AS frontend-build

WORKDIR /app/frontend

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/. .
RUN npm run build

FROM python:3.14-slim-bookworm AS backend-build

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app/backend

COPY backend/pyproject.toml backend/uv.lock ./
COPY backend/README.md ./
COPY backend/src ./src

RUN pip install --no-cache-dir uv \
    && uv sync --frozen --no-dev

FROM python:3.14-slim-bookworm AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FRONTEND_DIST_DIR=/app/frontend/dist

WORKDIR /app

COPY --from=backend-build /app/backend /app/backend
COPY --from=frontend-build /app/frontend/dist /app/frontend/dist

WORKDIR /app/backend

EXPOSE 8000

CMD ["/app/backend/.venv/bin/uvicorn", "certificate_app.main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "src"]
