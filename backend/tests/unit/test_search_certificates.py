from __future__ import annotations

import pytest

from certificate_app.application.dto.certificate_search import CertificateSearchQuery
from certificate_app.application.dto.provider_certificate import (
    ProviderCertificateDTO,
    ProviderCertificateSearchResponseDTO,
)
from certificate_app.application.use_cases.search_certificates import (
    SearchCertificatesUseCase,
)
from certificate_app.domain.value_objects.certificate_filter import CertificateFilter


class StubProvider:
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
                    certificate_url="https://example.com/cert.pdf",
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


@pytest.mark.asyncio
async def test_use_case_filters_success() -> None:
    use_case = SearchCertificatesUseCase(provider=StubProvider())
    result = await use_case.execute(
        CertificateSearchQuery(
            email="teste@gmail.com",
            status_filter=CertificateFilter.SUCCESS,
        )
    )
    assert result.filtered_count == 1
    assert result.certificates[0].success is True
