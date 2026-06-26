"""Controller helpers for certificate responses."""

from __future__ import annotations

from certificate_app.application.dto.certificate_search import CertificateSearchResult
from certificate_app.interface.schemas.certificates import CertificateSearchResponse


def map_result_to_response(result: CertificateSearchResult) -> CertificateSearchResponse:
    """Map use-case result into public API response."""
    return CertificateSearchResponse.model_validate(result.model_dump())
