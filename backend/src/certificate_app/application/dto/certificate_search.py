"""Application DTOs for certificate search."""

from __future__ import annotations

from pydantic import BaseModel, EmailStr

from certificate_app.domain.entities.certificate import Certificate
from certificate_app.domain.value_objects.certificate_filter import CertificateFilter


class CertificateSearchQuery(BaseModel):
    """Query sent to the use case."""

    email: EmailStr
    status_filter: CertificateFilter = CertificateFilter.ALL


class CertificateSearchResult(BaseModel):
    """Search result returned by the use case."""

    email: EmailStr
    applied_filter: CertificateFilter
    total_count: int
    filtered_count: int
    has_success: bool
    has_failed: bool
    certificates: list[Certificate]
