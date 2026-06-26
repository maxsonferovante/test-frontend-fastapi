"""DTOs mirroring provider responses."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, HttpUrl


class ProviderCertificateDTO(BaseModel):
    """Provider-side certificate payload."""

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


class ProviderCertificateSearchResponseDTO(BaseModel):
    """Provider response payload."""

    email: EmailStr
    certificates: list[ProviderCertificateDTO]
