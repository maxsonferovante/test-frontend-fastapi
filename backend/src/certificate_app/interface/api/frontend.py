"""Frontend serving integration."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI


def register_frontend(app: FastAPI, dist_dir: Path) -> None:
    """Register the built frontend with FastAPI."""
    app.frontend("/", directory=str(dist_dir), check_dir=False)
