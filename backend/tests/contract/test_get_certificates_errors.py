from __future__ import annotations

from fastapi.testclient import TestClient

from certificate_app.application.ports.certificate_provider import CertificateProvider
from certificate_app.domain.exceptions import (
    ProviderTimeoutError,
    ProviderUnavailableError,
)
from certificate_app.main import create_app


class TimeoutProvider(CertificateProvider):
    async def fetch_certificates(self, email: str):  # type: ignore[override]
        raise ProviderTimeoutError("Provider request timed out.")


class UnavailableProvider(CertificateProvider):
    async def fetch_certificates(self, email: str):  # type: ignore[override]
        raise ProviderUnavailableError("Provider is unavailable.")


def build_client(provider: CertificateProvider) -> TestClient:
    app = create_app()
    app.dependency_overrides.clear()
    from certificate_app.interface.api.certificates import get_search_use_case
    from certificate_app.application.use_cases.search_certificates import (
        SearchCertificatesUseCase,
    )

    app.dependency_overrides[get_search_use_case] = lambda: SearchCertificatesUseCase(
        provider
    )
    return TestClient(app)


def test_invalid_email_returns_422() -> None:
    client = build_client(UnavailableProvider())
    response = client.get("/api/v1/certificates", params={"email": "invalid"})
    assert response.status_code == 422


def test_timeout_error_returns_503() -> None:
    client = build_client(TimeoutProvider())
    response = client.get("/api/v1/certificates", params={"email": "teste@gmail.com"})
    assert response.status_code == 503


def test_provider_unavailable_returns_503() -> None:
    client = build_client(UnavailableProvider())
    response = client.get("/api/v1/certificates", params={"email": "teste@gmail.com"})
    assert response.status_code == 503
