# Backend

## Environment variables

- `CERTIFICATE_API_BASE_URL`: base URL da API externa. Default:
  `https://SUA_URL_AQUI`
- `CERTIFICATE_API_STAGE`: stage da API externa. Default: `dev`
- `CERTIFICATE_API_KEY`: chave obrigatoria para autenticar no provedor externo
- `CERTIFICATE_API_TIMEOUT_SECONDS`: timeout de rede. Default: `10`
- `FRONTEND_DIST_DIR`: caminho opcional para o build do frontend

## Commands

```bash
uv sync
uv run python -m uvicorn certificate_app.main:app --host 127.0.0.1 --port 8000 --app-dir src --reload
uv run pytest
```

O backend carrega o arquivo `.env` da raiz do repositorio.

## Docker

Na imagem unica, o frontend compilado e servido pelo mesmo processo FastAPI.

```bash
docker build -t certificate-app:local ..
docker run --rm --env-file ../.env -p 8000:8000 certificate-app:local
```
