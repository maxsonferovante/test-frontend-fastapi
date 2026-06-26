"""HTTP implementation of the certificate provider port."""

from __future__ import annotations

from urllib.parse import quote

import httpx
from pydantic import ValidationError

from certificate_app.application.dto.provider_certificate import (
    ProviderCertificateSearchResponseDTO,
)
from certificate_app.domain.exceptions import ProviderError, ProviderTimeoutError, ProviderUnavailableError
from certificate_app.infrastructure.config.settings import Settings
from certificate_app.observability.logging import get_logger


class HttpCertificateProvider:
    """Fetch certificate data from the remote provider."""

    def __init__(self, settings: Settings, client: httpx.AsyncClient | None = None) -> None:
        self._settings = settings
        self._client = client
        self._logger = get_logger("provider")

    async def fetch_certificates(self, email: str) -> ProviderCertificateSearchResponseDTO:
        """Fetch certificates from the configured provider."""
        url = f"{self._settings.provider_certificates_url}/{quote(email, safe='')}/certificates"
        headers = {"x-api-key": self._settings.certificate_api_key}
        timeout = httpx.Timeout(self._settings.certificate_api_timeout_seconds)
        try:
            if self._client is None:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.get(url, headers=headers)
            else:
                response = await self._client.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
        except httpx.TimeoutException as exc:
            self._logger.warning("provider timeout", extra={"email": email})
            raise ProviderTimeoutError("Provider request timed out.") from exc
        except httpx.HTTPStatusError as exc:
            self._logger.warning(
                "provider http error",
                extra={"email": email, "status_code": exc.response.status_code},
            )
            raise ProviderUnavailableError("Provider returned an unexpected status.") from exc
        except httpx.HTTPError as exc:
            self._logger.warning("provider transport error", extra={"email": email})
            raise ProviderUnavailableError("Provider is unavailable.") from exc
        try:
            return ProviderCertificateSearchResponseDTO.model_validate(response.json())
        except (ValueError, ValidationError) as exc:
            self._logger.error("provider invalid payload", extra={"email": email})
            raise ProviderError("Provider returned an invalid payload.") from exc
