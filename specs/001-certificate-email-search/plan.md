# Implementation Plan: Listagem de Certificados por Email

**Branch**: `[001-certificate-email-search]` | **Date**: 2026-06-26 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-certificate-email-search/spec.md`

## Summary

Construir uma aplicacao web com backend FastAPI e frontend React para consultar certificados por email, aplicar filtro por resultado (`all`, `success`, `failed`) e servir o build estatico do frontend pelo proprio FastAPI usando `app.frontend()`. A entrega operacional sera uma unica imagem Docker com build multi-stage, contendo o frontend compilado e o backend pronto para servir a SPA e a API interna no mesmo processo HTTP.

## Technical Context

**Language/Version**: Backend em Python 3.14; frontend em TypeScript 5.8.x com React 19.1

**Primary Dependencies**: FastAPI 0.138.1, Pydantic Settings 2.10.x, HTTPX 0.28.x, Uvicorn 0.35.x, React Router 7.18.0, Chakra UI 3.27.x, Tailwind CSS v4, componentes shadcn/ui

**Storage**: N/A para v1; dados consultados em tempo real na API externa

**Testing**: `pytest`, `pytest-asyncio`, `httpx` para backend; `vitest`, `@testing-library/react`, `playwright` para frontend e fluxo E2E; smoke validation por `docker build` e `docker run` para a entrega unificada

**Target Platform**: Aplicacao web full-stack servida por processo FastAPI em ambiente Linux e distribuida como imagem Docker unica

**Project Type**: Web application com frontend estatico e backend HTTP

**Performance Goals**: resposta conclusiva para buscas validas em ate 10 segundos; alternancia de filtro sem nova chamada externa quando aplicada sobre a mesma resposta; primeira pintura da tela principal apos assets carregados em ate 3 segundos em ambiente local; inicializacao da imagem unica com aplicacao acessivel em ate 15 minutos conforme a spec

**Constraints**: preservar chave da API apenas no backend; nao expor endpoint externo diretamente ao navegador; respeitar Clean Architecture no backend; frontend precisa funcionar com roteamento client-side servido por `app.frontend()`; ausencia de banco de dados nesta fase; a distribuicao deve ocorrer em uma unica imagem Docker sem depender de container separado para assets ou proxy reverso

**Scale/Scope**: uma tela principal de busca; um endpoint interno de consulta; ate centenas de certificados por email em leitura; um provedor externo de certificados; um artefato de deploy unico na raiz do repositorio

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Passa em corretude Pythonica: o plano mantem backend tipado, com contratos explicitos, `src/` layout e configuracao central em `pyproject.toml`.
- Passa em Clean Architecture: a chamada HTTP externa fica em `infrastructure/external_services`, o caso de uso fica em `application/use_cases` e a interface HTTP apenas adapta entrada e saida.
- Passa em SOLID: o facade do provedor externo fica isolado atras de uma porta de aplicacao, evitando acoplamento do dominio com HTTP.
- Passa em qualidade e testes: o plano preve testes unitarios, integracao/contrato e E2E do fluxo principal.
- Passa em simplicidade e observabilidade: sem persistencia local nesta fase, com logging estruturado, politica explicita de timeout/falha no cliente externo e empacotamento unico sem introduzir infraestrutura adicional.
- Nenhuma violacao exige justificativa nesta fase.

## Project Structure

### Documentation (this feature)

```text
specs/001-certificate-email-search/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── backend-openapi.yaml
│   └── external-provider.md
└── tasks.md
```

### Source Code (repository root)

```text
Dockerfile
.dockerignore
.env

backend/
├── pyproject.toml
├── src/
│   └── certificate_app/
│       ├── domain/
│       │   ├── entities/
│       │   ├── value_objects/
│       │   └── exceptions.py
│       ├── application/
│       │   ├── dto/
│       │   ├── ports/
│       │   └── use_cases/
│       ├── interface/
│       │   ├── api/
│       │   ├── controllers/
│       │   └── schemas/
│       ├── infrastructure/
│       │   ├── config/
│       │   └── external_services/
│       ├── observability/
│       └── main.py
└── tests/
    ├── contract/
    ├── integration/
    └── unit/

frontend/
├── package.json
├── tsconfig.json
├── vite.config.ts
├── src/
│   ├── app/
│   ├── features/
│   │   └── certificate-search/
│   ├── lib/
│   ├── routes/
│   └── styles/
└── tests/
    ├── integration/
    └── unit/

tests/
└── e2e/
```

**Structure Decision**: adotar estrutura web app com `backend/` e `frontend/` separados, mantendo o backend organizado segundo a constituicao Clean Architecture, o frontend como SPA estaticamente compilada e servida pelo FastAPI, e um `Dockerfile` raiz para produzir a imagem unica de distribuicao.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
