"""Application and domain exceptions for certificate search."""

from __future__ import annotations


class CertificateAppError(Exception):
    """Base application error."""


class InvalidEmailError(CertificateAppError):
    """Raised when an email query is invalid."""


class ProviderError(CertificateAppError):
    """Raised when the provider returns an unusable response."""


class ProviderTimeoutError(ProviderError):
    """Raised when provider access times out."""


class ProviderUnavailableError(ProviderError):
    """Raised when provider access fails due to transport or availability issues."""
