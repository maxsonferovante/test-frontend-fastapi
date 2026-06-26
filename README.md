# Certificate Search App

Aplicacao full-stack para buscar certificados por email, visualizar resultados
com sucesso ou sem sucesso e servir o frontend estatico pelo proprio FastAPI.

## Estrutura

- `backend/`: API FastAPI, integracao com o provedor externo e servico de assets
- `frontend/`: SPA React com Chakra UI, React Router e estilos em Tailwind v4
- `tests/e2e/`: fluxos end-to-end criticos
- `Dockerfile`: imagem unica multi-stage para distribuir backend e frontend juntos

## Variaveis de ambiente

- `CERTIFICATE_API_KEY`: obrigatoria para acessar a API externa
- `CERTIFICATE_API_BASE_URL`: opcional, default da API de certificados
- `CERTIFICATE_API_STAGE`: opcional, default `dev`
- `CERTIFICATE_API_TIMEOUT_SECONDS`: opcional, default `10`
- `VITE_API_BASE_URL`: opcional no frontend; se ausente usa a origem atual

O arquivo `.env` deve ficar na raiz do repositorio.

## Comandos

### Backend

```bash
cd backend
uv sync
uv run fastapi dev src/certificate_app/main.py
uv run pytest
```

Ou, a partir da raiz do repositório:

```bash
uv run --directory backend python -m uvicorn certificate_app.main:app --host 127.0.0.1 --port 8000 --app-dir src --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
npm run test
```

### E2E

```bash
cd frontend
npm run test:e2e
```

### Docker

```bash
docker build -t certificate-app:local .
docker run --rm --env-file .env -p 8000:8000 certificate-app:local
```

### Smoke do container

```bash
docker run --rm -d --name certificate-app-smoke -p 8012:8000 -e CERTIFICATE_USE_MOCK_PROVIDER=true certificate-app:local
curl --fail --silent --show-error http://127.0.0.1:8012/
curl --fail --silent --show-error http://127.0.0.1:8012/search/certificate
docker stop certificate-app-smoke
```
