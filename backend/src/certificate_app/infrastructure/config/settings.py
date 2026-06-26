"""Settings for external provider and frontend serving."""

from __future__ import annotations

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    _repo_root = Path(__file__).resolve().parents[5]

    model_config = SettingsConfigDict(
        env_file=_repo_root / ".env",
        env_prefix="",
        extra="ignore",
    )

    certificate_api_base_url: str = "https://SUA_URL_AQUI"
    certificate_api_stage: str = "dev"
    certificate_api_key: str = Field("", alias="CERTIFICATE_API_KEY")
    certificate_api_timeout_seconds: float = 10.0
    certificate_use_mock_provider: bool = False
    frontend_dist_dir: str | None = None

    @property
    def provider_certificates_url(self) -> str:
        """Base URL for provider certificate listing."""
        return (
            f"{self.certificate_api_base_url.rstrip('/')}/"
            f"{self.certificate_api_stage}/api/v1/users"
        )

    @property
    def resolved_frontend_dist_dir(self) -> Path:
        """Resolve the frontend dist directory relative to the repo root."""
        if self.frontend_dist_dir:
            configured_path = Path(self.frontend_dist_dir).expanduser()
            if configured_path.is_absolute():
                return configured_path.resolve()

            candidates = [
                (Path.cwd() / configured_path).resolve(),
                (self._repo_root / configured_path).resolve(),
            ]
            for candidate in candidates:
                if candidate.exists():
                    return candidate
            return candidates[0]
        return self._repo_root / "frontend" / "dist"


def get_settings() -> Settings:
    """Return settings instance."""
    return Settings()
