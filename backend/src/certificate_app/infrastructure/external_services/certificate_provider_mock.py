"""Mock provider used for local end-to-end validation."""

from __future__ import annotations

from certificate_app.application.dto.provider_certificate import (
    ProviderCertificateDTO,
    ProviderCertificateSearchResponseDTO,
)


class MockCertificateProvider:
    """Return deterministic certificate payloads for local validation."""

    async def fetch_certificates(self, email: str) -> ProviderCertificateSearchResponseDTO:
        if email == "empty@example.com":
            return ProviderCertificateSearchResponseDTO(email=email, certificates=[])
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
                    certificate_url="https://example.com/certificate.pdf",
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
