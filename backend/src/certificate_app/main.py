"""FastAPI application entrypoint."""

from __future__ import annotations

from fastapi import FastAPI

from certificate_app.application.use_cases.search_certificates import SearchCertificatesUseCase
from certificate_app.infrastructure.config.settings import get_settings
from certificate_app.infrastructure.external_services.certificate_provider_http import (
    HttpCertificateProvider,
)
from certificate_app.infrastructure.external_services.certificate_provider_mock import (
    MockCertificateProvider,
)
from certificate_app.interface.api import certificates
from certificate_app.interface.api.certificates import router as certificates_router
from certificate_app.interface.api.error_handlers import register_error_handlers
from certificate_app.interface.api.frontend import register_frontend
from certificate_app.observability.logging import configure_logging


def create_app() -> FastAPI:
    """Build the FastAPI app."""
    configure_logging()
    settings = get_settings()
    provider = (
        MockCertificateProvider()
        if settings.certificate_use_mock_provider
        else HttpCertificateProvider(settings=settings)
    )
    use_case = SearchCertificatesUseCase(provider=provider)

    app = FastAPI(title="Certificate Search App", version="0.1.0")
    register_error_handlers(app)

    def _get_search_use_case() -> SearchCertificatesUseCase:
        return use_case

    certificates.configure_search_use_case(_get_search_use_case)
    app.include_router(certificates_router)
    register_frontend(app, settings.resolved_frontend_dist_dir)
    return app


app = create_app()
