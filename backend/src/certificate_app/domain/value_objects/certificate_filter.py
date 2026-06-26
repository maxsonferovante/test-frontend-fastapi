"""Value objects for certificate filtering."""

from __future__ import annotations

from enum import StrEnum


class CertificateFilter(StrEnum):
    """Allowed filters for certificate search."""

    ALL = "all"
    SUCCESS = "success"
    FAILED = "failed"
