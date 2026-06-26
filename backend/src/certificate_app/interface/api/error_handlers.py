"""HTTP exception handlers."""

from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from certificate_app.domain.exceptions import (
    InvalidEmailError,
    ProviderError,
    ProviderTimeoutError,
    ProviderUnavailableError,
)
from certificate_app.interface.schemas.certificates import ErrorResponse


def register_error_handlers(app: FastAPI) -> None:
    """Register HTTP exception handlers."""

    @app.exception_handler(InvalidEmailError)
    async def handle_invalid_email(_: Request, exc: InvalidEmailError) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content=ErrorResponse(code="invalid_email", message=str(exc)).model_dump(),
        )

    @app.exception_handler(ProviderTimeoutError)
    async def handle_provider_timeout(_: Request, exc: ProviderTimeoutError) -> JSONResponse:
        return JSONResponse(
            status_code=503,
            content=ErrorResponse(code="provider_timeout", message=str(exc)).model_dump(),
        )

    @app.exception_handler(ProviderUnavailableError)
    async def handle_provider_unavailable(
        _: Request,
        exc: ProviderUnavailableError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=503,
            content=ErrorResponse(code="provider_unavailable", message=str(exc)).model_dump(),
        )

    @app.exception_handler(ProviderError)
    async def handle_provider_error(_: Request, exc: ProviderError) -> JSONResponse:
        return JSONResponse(
            status_code=502,
            content=ErrorResponse(code="provider_error", message=str(exc)).model_dump(),
        )
