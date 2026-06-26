"""HTTP schemas for certificate search."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, HttpUrl

from certificate_app.domain.value_objects.certificate_filter import CertificateFilter


class CertificateResponse(BaseModel):
    """Certificate item response."""

    id: UUID
    order_id: int
    product_id: int
    participant_name: str
    participant_email: EmailStr
    participant_document: str
    certificate_url: HttpUrl | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    success: bool


class CertificateSearchResponse(BaseModel):
    """Certificate search response."""

    email: EmailStr
    applied_filter: CertificateFilter
    total_count: int
    filtered_count: int
    has_success: bool
    has_failed: bool
    certificates: list[CertificateResponse]


class ErrorResponse(BaseModel):
    """Public error response."""

    code: str
    message: str
