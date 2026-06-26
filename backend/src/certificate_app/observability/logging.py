"""Logging helpers."""

from __future__ import annotations

import logging


def configure_logging() -> None:
    """Configure root logging once for the app."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def get_logger(name: str) -> logging.Logger:
    """Return a namespaced logger."""
    return logging.getLogger(f"certificate_app.{name}")
