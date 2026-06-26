from __future__ import annotations

from fastapi.testclient import TestClient

from certificate_app.application.dto.provider_certificate import (
    ProviderCertificateDTO,
    ProviderCertificateSearchResponseDTO,
)
from certificate_app.application.ports.certificate_provider import CertificateProvider
from certificate_app.main import create_app


class FakeProvider(CertificateProvider):
    async def fetch_certificates(
        self, email: str
    ) -> ProviderCertificateSearchResponseDTO:
        return ProviderCertificateSearchResponseDTO(
            email=email,
            certificates=[
                ProviderCertificateDTO(
                    id="060d543f-7c44-4370-97c6-ca54cae0bfc2",
                    order_id=3340,
                    product_id=3336,
                    participant_name="Maxson Almeida",
                    participant_email=email,
                    participant_document="",
                    certificate_url=(
                        "https://SUA_URL_AQUI/"
                        "dev/api/v1/certificate/download?id=060d543f-7c44-4370-97c6-ca54cae0bfc2"
                    ),
                    created_at="2025-12-06T17:57:07.693972",
                    updated_at="2025-12-06T17:57:07.693972",
                    success=True,
                ),
                ProviderCertificateDTO(
                    id="b21c7fc8-ed52-4ee8-8267-3b01fdbc7c59",
                    order_id=3272,
                    product_id=316,
                    participant_name="Maxson Almeida Ferovante",
                    participant_email=email,
                    participant_document="",
                    certificate_url=None,
                    created_at=None,
                    updated_at=None,
                    success=False,
                ),
            ],
        )


def build_client() -> TestClient:
    app = create_app()
    app.dependency_overrides.clear()
    from certificate_app.interface.api.certificates import get_search_use_case
    from certificate_app.application.use_cases.search_certificates import (
        SearchCertificatesUseCase,
    )

    app.dependency_overrides[get_search_use_case] = lambda: SearchCertificatesUseCase(
        FakeProvider()
    )
    return TestClient(app)


def test_get_certificates_success() -> None:
    client = build_client()
    response = client.get("/api/v1/certificates", params={"email": "teste@gmail.com"})
    assert response.status_code == 200
    payload = response.json()
    assert payload["email"] == "teste@gmail.com"
    assert payload["total_count"] == 2
    assert payload["filtered_count"] == 2


def test_get_certificates_filtered_status() -> None:
    client = build_client()
    response = client.get(
        "/api/v1/certificates",
        params={"email": "teste@gmail.com", "status": "success"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["applied_filter"] == "success"
    assert payload["filtered_count"] == 1
    assert payload["certificates"][0]["success"] is True
