from __future__ import annotations

import httpx
import pytest

from certificate_app.domain.exceptions import ProviderError, ProviderTimeoutError
from certificate_app.infrastructure.config.settings import Settings
from certificate_app.infrastructure.external_services.certificate_provider_http import (
    HttpCertificateProvider,
)


@pytest.mark.asyncio
async def test_provider_http_maps_success_payload() -> None:
    payload = {
        "email": "teste@gmail.com",
        "certificates": [
            {
                "id": "060d543f-7c44-4370-97c6-ca54cae0bfc2",
                "order_id": 3340,
                "product_id": 3336,
                "participant_name": "Maxson Almeida",
                "participant_email": "teste@gmail.com",
                "participant_document": "",
                "certificate_url": "https://example.com/certificate.pdf",
                "created_at": "2025-12-06T17:57:07.693972",
                "updated_at": "2025-12-06T17:57:07.693972",
                "success": True,
            }
        ],
    }

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=payload)

    transport = httpx.MockTransport(handler)
    async with httpx.AsyncClient(transport=transport) as client:
        provider = HttpCertificateProvider(
            settings=Settings(CERTIFICATE_API_KEY="secret"),
            client=client,
        )
        result = await provider.fetch_certificates("teste@gmail.com")
    assert result.email == "teste@gmail.com"
    assert len(result.certificates) == 1


@pytest.mark.asyncio
async def test_provider_http_raises_on_invalid_payload() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"invalid": "payload"})

    transport = httpx.MockTransport(handler)
    async with httpx.AsyncClient(transport=transport) as client:
        provider = HttpCertificateProvider(
            settings=Settings(CERTIFICATE_API_KEY="secret"),
            client=client,
        )
        with pytest.raises(ProviderError):
            await provider.fetch_certificates("teste@gmail.com")


@pytest.mark.asyncio
async def test_provider_http_raises_on_timeout() -> None:
    async def fake_get(*args, **kwargs):
        raise httpx.ReadTimeout("timeout")

    client = httpx.AsyncClient()
    client.get = fake_get  # type: ignore[method-assign]
    provider = HttpCertificateProvider(
        settings=Settings(CERTIFICATE_API_KEY="secret"),
        client=client,
    )
    with pytest.raises(ProviderTimeoutError):
        await provider.fetch_certificates("teste@gmail.com")
