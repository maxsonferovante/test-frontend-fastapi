"""Use case for certificate search."""

from __future__ import annotations

from certificate_app.application.dto.certificate_search import (
    CertificateSearchQuery,
    CertificateSearchResult,
)
from certificate_app.application.dto.provider_certificate import ProviderCertificateDTO
from certificate_app.application.ports.certificate_provider import CertificateProvider
from certificate_app.domain.entities.certificate import Certificate
from certificate_app.domain.value_objects.certificate_filter import CertificateFilter


class SearchCertificatesUseCase:
    """Search certificates and apply result filtering."""

    def __init__(self, provider: CertificateProvider) -> None:
        self._provider = provider

    async def execute(self, query: CertificateSearchQuery) -> CertificateSearchResult:
        """Fetch and filter certificates for the target email."""
        provider_response = await self._provider.fetch_certificates(str(query.email))
        all_certificates = [
            self._map_provider_certificate(item)
            for item in provider_response.certificates
        ]
        filtered = self._apply_filter(all_certificates, query.status_filter)
        return CertificateSearchResult(
            email=provider_response.email,
            applied_filter=query.status_filter,
            total_count=len(all_certificates),
            filtered_count=len(filtered),
            has_success=any(item.success for item in all_certificates),
            has_failed=any(not item.success for item in all_certificates),
            certificates=filtered,
        )

    @staticmethod
    def _map_provider_certificate(provider_certificate: ProviderCertificateDTO) -> Certificate:
        return Certificate.model_validate(provider_certificate.model_dump())

    @staticmethod
    def _apply_filter(
        certificates: list[Certificate],
        status_filter: CertificateFilter,
    ) -> list[Certificate]:
        if status_filter is CertificateFilter.ALL:
            return certificates
        if status_filter is CertificateFilter.SUCCESS:
            return [item for item in certificates if item.success]
        return [item for item in certificates if not item.success]
