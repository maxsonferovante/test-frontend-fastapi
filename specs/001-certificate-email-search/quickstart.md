# Quickstart: Listagem de Certificados por Email

## Prerequisites

- Python 3.14 disponivel localmente
- Node.js 22+ e npm
- Variavel de ambiente `CERTIFICATE_API_KEY` configurada com a chave do provedor externo
- Acesso de rede ao endpoint `https://mpl8es0cb7.execute-api.us-east-1.amazonaws.com`

## Suggested Workspace Setup

### Backend

```bash
cd backend
uv sync
uv run fastapi dev src/certificate_app/main.py
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
2. Informar `maxsonferovante@gmail.com`.
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
npm run test:e2e
```

## Expected Outcomes

- O backend rejeita emails invalidos com erro `400`.
- O backend nao expoe `x-api-key` ao frontend.
- O frontend apresenta estados de carregamento, vazio, erro e sucesso.
- O filtro alterna a visualizacao sem nova consulta externa para a mesma resposta carregada.
