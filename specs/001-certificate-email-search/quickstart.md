# Quickstart: Listagem de Certificados por Email

## Prerequisites

- Python 3.14 disponivel localmente
- Node.js 22+ e npm
- `uv` instalado para sincronizar dependencias Python
- Docker disponivel localmente para validar a imagem unica
- Arquivo `.env` na raiz do repositorio com `CERTIFICATE_API_KEY` e URL base do provedor configuradas
- Acesso de rede ao endpoint do provedor externo documentado em [external-provider.md](./contracts/external-provider.md)

## Suggested Workspace Setup

### Backend

```bash
uv sync --directory backend
uv run --directory backend python -m uvicorn certificate_app.main:app --host 127.0.0.1 --port 8000 --app-dir src --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## End-to-End Validation Flow

### Scenario 1: Busca com resultados mistos

1. Abrir a aplicacao web.
2. Informar `teste@gmail.com`.
3. Executar a busca.
4. Confirmar que a interface exibe pelo menos um certificado com `success=true` e um com `success=false`.
5. Aplicar o filtro `success` e validar que apenas certificados bem-sucedidos permanecem visiveis.
6. Aplicar o filtro `failed` e validar que apenas certificados sem sucesso permanecem visiveis.

### Scenario 2: Email sem resultados

1. Informar um email valido sem certificados.
2. Executar a busca.
3. Confirmar mensagem de estado vazio sem quebrar a navegacao.

### Scenario 3: Email invalido

1. Informar um texto fora do formato de email.
2. Confirmar bloqueio da submissao ou mensagem de validacao antes da chamada ao backend.

### Scenario 4: Frontend servido pelo FastAPI

1. Gerar o build do frontend:

```bash
cd frontend
npm run build
```

2. Iniciar apenas o backend em modo local.
3. Acessar `http://127.0.0.1:8000/`.
4. Confirmar que a SPA e servida pelo FastAPI.
5. Navegar diretamente para uma rota client-side e confirmar fallback para `index.html`.

### Scenario 5: Imagem Docker unica da aplicacao

1. Gerar o build do frontend para disponibilizar os assets que serao empacotados:

```bash
cd frontend
npm install
npm run build
```

2. Construir a imagem unica na raiz do repositorio:

```bash
docker build -t certificate-app:local .
```

3. Iniciar a imagem apontando para o arquivo `.env` da raiz:

```bash
docker run --rm --env-file .env -p 8000:8000 certificate-app:local
```

4. Acessar `http://127.0.0.1:8000/`.
5. Confirmar que a interface e a busca de certificados funcionam no mesmo endereco exposto pela imagem.
6. Confirmar que nao e necessario iniciar frontend e backend separadamente para usar a aplicacao.

## Contract Validation

- Validar o contrato interno em [backend-openapi.yaml](./contracts/backend-openapi.yaml).
- Validar o mapeamento do provedor externo em [external-provider.md](./contracts/external-provider.md).

## Test Commands

```bash
cd backend
uv run pytest
```

```bash
cd frontend
npm run test
```

```bash
cd frontend
npm run test:e2e
```

```bash
docker build -t certificate-app:local .
```

## Expected Outcomes

- O backend rejeita emails invalidos com erro `400`.
- O backend nao expoe `x-api-key` ao frontend.
- O frontend apresenta estados de carregamento, vazio, erro e sucesso.
- O filtro alterna a visualizacao sem nova consulta externa para a mesma resposta carregada.
- A imagem Docker unica sobe a aplicacao completa com a SPA servida pelo FastAPI no mesmo endpoint HTTP.
