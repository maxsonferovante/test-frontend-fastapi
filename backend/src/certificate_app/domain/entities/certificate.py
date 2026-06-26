"""Domain entity representing a certificate."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, HttpUrl


class Certificate(BaseModel):
    """Certificate result returned by the provider."""

    model_config = ConfigDict(frozen=True)

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
