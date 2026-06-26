"""API endpoints for certificates."""

from __future__ import annotations

from collections.abc import Callable

from fastapi import APIRouter, Depends, Query
from pydantic import EmailStr

from certificate_app.application.dto.certificate_search import CertificateSearchQuery
from certificate_app.application.use_cases.search_certificates import SearchCertificatesUseCase
from certificate_app.domain.value_objects.certificate_filter import CertificateFilter
from certificate_app.interface.controllers.certificates import map_result_to_response
from certificate_app.interface.schemas.certificates import CertificateSearchResponse

router = APIRouter(prefix="/api/v1/certificates", tags=["certificates"])
_search_use_case_factory: Callable[[], SearchCertificatesUseCase] | None = None


def get_search_use_case() -> SearchCertificatesUseCase:
    """Return the configured search use case."""
    if _search_use_case_factory is None:
        raise RuntimeError("Search use case dependency not configured.")
    return _search_use_case_factory()


def configure_search_use_case(factory: Callable[[], SearchCertificatesUseCase]) -> None:
    """Configure the dependency factory for certificate search."""
    global _search_use_case_factory
    _search_use_case_factory = factory


@router.get("", response_model=CertificateSearchResponse)
async def list_certificates(
    email: EmailStr = Query(...),
    status: CertificateFilter = Query(CertificateFilter.ALL),
    use_case: SearchCertificatesUseCase = Depends(get_search_use_case),
) -> CertificateSearchResponse:
    """List certificates for the target email."""
    query = CertificateSearchQuery(email=email, status_filter=status)
    result = await use_case.execute(query)
    return map_result_to_response(result)
