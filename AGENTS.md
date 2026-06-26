# Repository Guidelines

## Project Structure & Module Organization
- `backend/`: FastAPI service, domain/application/infrastructure layers, and backend tests in `backend/tests/`.
- `frontend/`: React + React Router UI, Chakra components, and frontend tests in `frontend/tests/`.
- `tests/e2e/`: end-to-end checks for the full app flow and packaged container flow.
- `specs/001-certificate-email-search/`: Spec Kit artifacts (`spec.md`, `plan.md`, `tasks.md`, `quickstart.md`, contracts).
- Root files: `Dockerfile`, `.dockerignore`, `.env`, `README.md`, and this guide.

## Build, Test, and Development Commands
- `uv run --directory backend python -m uvicorn certificate_app.main:app --host 127.0.0.1 --port 8000 --app-dir src --reload`: run the backend locally.
- `cd frontend && npm run dev`: run the frontend dev server.
- `cd frontend && npm run test`: run unit and integration tests.
- `cd frontend && npm run test:e2e`: run Playwright E2E checks through the packaged test runner.
- `UV_CACHE_DIR=/tmp/uv-cache uv run --directory backend pytest`: run backend tests.
- `docker build -t certificate-app:local .` and `docker run --rm --env-file .env -p 8000:8000 certificate-app:local`: validate the single-image delivery.

## Coding Style & Naming Conventions
- Python: 3.14+, type hints on public code, `ruff`-compatible formatting, `snake_case` for modules/functions, `PascalCase` for classes.
- TypeScript/React: `camelCase` for functions and variables, `PascalCase` for components, keep route and feature files under `frontend/src/features/` and `frontend/src/routes/`.
- Prefer small, focused modules that respect the existing backend layer boundaries.

## Testing Guidelines
- Backend tests use `pytest`; frontend tests use `vitest` and `@testing-library/react`; browser checks use Playwright.
- Keep tests deterministic and place them near the behavior they verify: `backend/tests/unit/`, `backend/tests/integration/`, `backend/tests/contract/`, `tests/e2e/`.
- Name tests by behavior, not implementation detail, for example `test_get_certificates_success`.

## Commit & Pull Request Guidelines
- Commit history uses short imperative messages, such as `feat: add single-image docker packaging` and `fix: resolve frontend dist path in docker`.
- Keep commits atomic: docs, packaging, and runtime fixes should be separate when practical.
- PRs should include a short summary, test evidence, and screenshots or notes if UI behavior changed.

## Security & Configuration Tips
- Keep secrets in the root `.env`; do not commit API keys.
- The backend reads `CERTIFICATE_API_KEY`, `CERTIFICATE_API_BASE_URL`, `CERTIFICATE_API_STAGE`, and `FRONTEND_DIST_DIR`.
- For container smoke checks, use the validated pattern from the README and stop the container after verification.
