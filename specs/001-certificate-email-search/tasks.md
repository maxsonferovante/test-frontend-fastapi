# Tasks: Listagem de Certificados por Email

**Input**: Design documents from `/specs/001-certificate-email-search/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Incluir testes unitarios, contrato, integracao e E2E por exigencia da constituicao e do plano.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Inicializar a estrutura full-stack e as ferramentas base do projeto

- [X] T001 Create backend project skeleton and Python packaging in backend/pyproject.toml
- [X] T002 [P] Create backend source and test directory structure in backend/src/certificate_app/ and backend/tests/
- [X] T003 [P] Create frontend project manifest and tooling baseline in frontend/package.json
- [X] T004 [P] Create frontend source and test directory structure in frontend/src/ and frontend/tests/
- [X] T005 Configure shared developer documentation and bootstrap commands in README.md

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Infraestrutura obrigatoria para qualquer historia funcionar

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Implement backend application entrypoint and FastAPI app factory in backend/src/certificate_app/main.py
- [X] T007 [P] Implement backend settings and secret loading for provider access in backend/src/certificate_app/infrastructure/config/settings.py
- [X] T008 [P] Implement structured logging and shared error types in backend/src/certificate_app/observability/logging.py and backend/src/certificate_app/domain/exceptions.py
- [X] T009 [P] Define core DTOs, value objects, and enums for certificate search in backend/src/certificate_app/application/dto/certificate_search.py and backend/src/certificate_app/domain/value_objects/certificate_filter.py
- [X] T010 Implement provider port and HTTP client adapter shell in backend/src/certificate_app/application/ports/certificate_provider.py and backend/src/certificate_app/infrastructure/external_services/certificate_provider_http.py
- [X] T011 [P] Implement shared API schemas and response mappers in backend/src/certificate_app/interface/schemas/certificates.py and backend/src/certificate_app/interface/controllers/certificates.py
- [X] T012 [P] Configure frontend app shell, router bootstrap, Chakra provider, and Tailwind v4 style entrypoints in frontend/src/app/router.tsx, frontend/src/app/providers.tsx, frontend/src/main.tsx, and frontend/src/styles/globals.css
- [X] T013 [P] Create reusable frontend API client, environment config, and query-state helpers in frontend/src/lib/api.ts, frontend/src/lib/config.ts, and frontend/src/lib/http-errors.ts
- [X] T014 Configure FastAPI frontend serving hook for compiled frontend assets in backend/src/certificate_app/interface/api/frontend.py and backend/src/certificate_app/main.py
- [X] T015 [P] Add backend and frontend baseline test configuration in backend/pyproject.toml, frontend/vitest.config.ts, frontend/playwright.config.ts, and tests/e2e/README.md

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Buscar certificados por email (Priority: P1) 🎯 MVP

**Goal**: Permitir busca por email e listagem completa de certificados retornados pelo provedor externo

**Independent Test**: Informar um email valido, executar a busca e ver a lista correspondente ou mensagem clara de nenhum resultado sem depender dos filtros adicionais

### Tests for User Story 1

- [X] T016 [P] [US1] Add provider adapter integration tests for success and empty responses in backend/tests/integration/test_certificate_provider_http.py
- [X] T017 [P] [US1] Add backend contract tests for GET /api/v1/certificates with valid email responses in backend/tests/contract/test_get_certificates.py
- [X] T018 [P] [US1] Add frontend integration tests for certificate search submission and result rendering in frontend/tests/integration/certificate-search-page.test.tsx
- [X] T019 [P] [US1] Add end-to-end MVP journey for searching a valid email in tests/e2e/certificate-search.spec.ts

### Implementation for User Story 1

- [X] T020 [P] [US1] Implement certificate entity and provider payload mapping in backend/src/certificate_app/domain/entities/certificate.py and backend/src/certificate_app/application/dto/provider_certificate.py
- [X] T021 [US1] Implement search certificates use case orchestrating provider calls in backend/src/certificate_app/application/use_cases/search_certificates.py
- [X] T022 [US1] Implement external provider HTTP client with timeout, auth header, and payload validation in backend/src/certificate_app/infrastructure/external_services/certificate_provider_http.py
- [X] T023 [US1] Implement certificates API endpoint and success/empty response mapping in backend/src/certificate_app/interface/api/certificates.py
- [X] T024 [P] [US1] Implement certificate search page layout and form components in frontend/src/features/certificate-search/search-form.tsx and frontend/src/routes/home.tsx
- [X] T025 [P] [US1] Implement certificate result list, item card, and empty state components in frontend/src/features/certificate-search/certificate-list.tsx, frontend/src/features/certificate-search/certificate-card.tsx, and frontend/src/features/certificate-search/empty-state.tsx
- [X] T026 [US1] Implement frontend search workflow and route integration in frontend/src/features/certificate-search/use-certificate-search.ts and frontend/src/routes/home.tsx
- [X] T027 [US1] Connect frontend search workflow to backend API client and render total search results in frontend/src/lib/api.ts and frontend/src/features/certificate-search/search-results-panel.tsx

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Filtrar por resultado do certificado (Priority: P2)

**Goal**: Permitir alternar entre todos, sucesso e falha sobre a resposta carregada da busca atual

**Independent Test**: Executar uma busca com resultados mistos e alternar os filtros vendo apenas os itens esperados sem nova consulta externa

### Tests for User Story 2

- [X] T028 [P] [US2] Extend backend contract tests for status query filtering in backend/tests/contract/test_get_certificates.py
- [X] T029 [P] [US2] Add frontend integration tests for local filter toggling and counts in frontend/tests/integration/certificate-filters.test.tsx
- [X] T030 [P] [US2] Extend end-to-end flow to validate success and failed filters in tests/e2e/certificate-search.spec.ts

### Implementation for User Story 2

- [X] T031 [US2] Implement filtered search result aggregation and count calculation in backend/src/certificate_app/application/use_cases/search_certificates.py
- [X] T032 [US2] Update API schemas to expose applied filter and summary counts in backend/src/certificate_app/interface/schemas/certificates.py
- [X] T033 [P] [US2] Implement filter switcher and result summary UI in frontend/src/features/certificate-search/filter-tabs.tsx and frontend/src/features/certificate-search/results-summary.tsx
- [X] T034 [US2] Implement client-side filtered result state management in frontend/src/features/certificate-search/use-certificate-search.ts
- [X] T035 [US2] Integrate filtered views into certificate results panel without re-fetching provider data in frontend/src/features/certificate-search/search-results-panel.tsx

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Entender estados vazios e erros de consulta (Priority: P3)

**Goal**: Exibir validacoes e mensagens claras para email invalido, indisponibilidade e estados sem resultados

**Independent Test**: Tentar buscar com email invalido, email sem resultados e falha temporaria do backend, verificando mensagens acionaveis em cada caso

### Tests for User Story 3

- [X] T036 [P] [US3] Add backend contract tests for invalid email, provider failure, and timeout handling in backend/tests/contract/test_get_certificates_errors.py
- [X] T037 [P] [US3] Add frontend integration tests for validation, empty, and error states in frontend/tests/integration/certificate-search-states.test.tsx
- [X] T038 [P] [US3] Extend end-to-end flow for invalid email and transient error messaging in tests/e2e/certificate-search-errors.spec.ts

### Implementation for User Story 3

- [X] T039 [P] [US3] Implement typed backend exceptions and HTTP error translation for provider failures in backend/src/certificate_app/domain/exceptions.py and backend/src/certificate_app/interface/api/error_handlers.py
- [X] T040 [US3] Add request validation and query parameter guarding for email and status in backend/src/certificate_app/interface/api/certificates.py
- [X] T041 [P] [US3] Implement frontend validation messaging and disabled submit states in frontend/src/features/certificate-search/search-form.tsx
- [X] T042 [P] [US3] Implement frontend loading, error, and retry feedback components in frontend/src/features/certificate-search/loading-state.tsx and frontend/src/features/certificate-search/error-state.tsx
- [X] T043 [US3] Integrate empty, invalid, and transient error states into the search page flow in frontend/src/routes/home.tsx and frontend/src/features/certificate-search/search-results-panel.tsx

**Checkpoint**: All user stories through US3 should now be independently functional

---

## Phase 6: User Story 4 - Disponibilizar a aplicacao em pacote unico portatil (Priority: P3)

**Goal**: Empacotar backend e frontend em uma unica imagem Docker pronta para subir a aplicacao completa

**Independent Test**: Construir a imagem a partir da raiz do repositorio, iniciar um unico container com `.env` e validar acesso a `http://127.0.0.1:8000/` com a SPA e a busca funcionando no mesmo endpoint

### Tests for User Story 4

- [X] T044 [P] [US4] Add backend integration coverage for frontend dist resolution used by the container runtime in backend/tests/integration/test_frontend_serving.py
- [X] T045 [P] [US4] Add end-to-end smoke validation for the packaged application startup flow in tests/e2e/docker-smoke.spec.ts

### Implementation for User Story 4

- [X] T046 [P] [US4] Create root multi-stage container build for frontend and backend in Dockerfile
- [X] T047 [P] [US4] Add container build context exclusions in .dockerignore
- [X] T048 [US4] Align backend runtime defaults for container startup and frontend asset serving in backend/src/certificate_app/infrastructure/config/settings.py and backend/src/certificate_app/main.py
- [X] T049 [US4] Document image build, run, and environment-file usage in README.md, backend/README.md, and specs/001-certificate-email-search/quickstart.md
- [X] T050 [US4] Validate the single-image workflow against specs/001-certificate-email-search/quickstart.md and record final command expectations in specs/001-certificate-email-search/tasks.md

**Checkpoint**: User Story 4 should provide a portable single-image deployment path without requiring separate frontend and backend startup

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Melhorias que atravessam multiplas historias

- [X] T051 [P] Refresh environment variables, run commands, and architecture notes in README.md and backend/README.md
- [X] T052 [P] Add focused unit tests for backend use case filtering logic and frontend result selectors in backend/tests/unit/test_search_certificates.py and frontend/tests/unit/certificate-selectors.test.ts
- [X] T053 Optimize frontend visual consistency with Chakra tokens and shadcn-inspired utility styles in frontend/src/styles/globals.css and frontend/src/features/certificate-search/certificate-card.tsx
- [X] T054 Harden security and observability around secret handling and request logging in backend/src/certificate_app/infrastructure/config/settings.py and backend/src/certificate_app/observability/logging.py
- [X] T055 Run full regression for backend, frontend, E2E, and Docker packaging via backend/tests/, frontend/tests/, tests/e2e/, and Dockerfile

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories 1-3 (Phases 3-5)**: Depend on Foundational completion
- **User Story 4 (Phase 6)**: Depends on Foundational completion and reuses the working flow from US1-US3 for packaging validation
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - defines the MVP
- **User Story 2 (P2)**: Depends on User Story 1 result loading flow being present
- **User Story 3 (P3)**: Depends on User Story 1 endpoint and UI flow, but remains independently testable once implemented
- **User Story 4 (P3)**: Depends on the integrated backend/frontend flow from User Stories 1-3 so the image can package the final application behavior

### Within Each User Story

- Tests should be authored before or alongside implementation and must validate observable behavior
- Domain and DTO mapping before use case orchestration
- Use case and adapter logic before endpoint/UI wiring
- Packaging tests before final smoke validation for the Docker image

### Parallel Opportunities

- Setup tasks T002, T003, and T004 can run in parallel after T001 starts the project baseline
- Foundational tasks T007, T008, T009, T012, T013, and T015 can run in parallel
- In US1, tests T016-T019 and UI tasks T024-T025 can run in parallel while backend core is built
- In US2, tests T028-T030 and UI summary/filter tasks T033 can run in parallel
- In US3, tests T036-T038 and UI feedback tasks T041-T042 can run in parallel
- In US4, tests T044-T045 and container-definition tasks T046-T047 can run in parallel before runtime alignment T048
- Polish tasks T051-T054 can run in parallel before final regression T055

---

## Parallel Example: User Story 4

```bash
# Launch User Story 4 validation scaffolding together:
Task: "Add backend integration coverage for frontend dist resolution in backend/tests/integration/test_frontend_serving.py"
Task: "Add end-to-end smoke validation for packaged startup in tests/e2e/docker-smoke.spec.ts"

# Launch User Story 4 packaging assets together:
Task: "Create root multi-stage container build in Dockerfile"
Task: "Add container build context exclusions in .dockerignore"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. Validate MVP with `tests/e2e/certificate-search.spec.ts`

### Incremental Delivery

1. Deliver User Story 1 for basic search and listagem
2. Add User Story 2 for local filtering over loaded results
3. Add User Story 3 for robust validation and operational feedback
4. Add User Story 4 for single-image Docker portability
5. Finish with full regression and packaging verification

### Parallel Team Strategy

1. Uma frente prepara backend foundation enquanto outra prepara frontend foundation
2. Depois da fundacao, backend e frontend de US1 podem avancar em paralelo
3. US2 e US3 podem ser divididas entre frontend/backend depois do MVP
4. US4 pode ser executada em paralelo por uma frente operacional apos a estabilizacao do fluxo integrado

---

## Notes

- Todos os itens seguem o formato estrito com checkbox, ID, labels opcionais e caminhos de arquivo
- Os labels `[US1]`, `[US2]`, `[US3]` e `[US4]` aparecem apenas nas fases de historia
- O escopo de MVP sugerido continua sendo a **User Story 1**
