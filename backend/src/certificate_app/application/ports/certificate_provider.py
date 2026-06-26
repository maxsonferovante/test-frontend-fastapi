"""Ports for certificate provider access."""

from __future__ import annotations

from typing import Protocol

from certificate_app.application.dto.provider_certificate import (
    ProviderCertificateSearchResponseDTO,
)


class CertificateProvider(Protocol):
    """External certificate provider access."""

    async def fetch_certificates(
        self,
        email: str,
    ) -> ProviderCertificateSearchResponseDTO:
        """Fetch certificates for the given email."""
