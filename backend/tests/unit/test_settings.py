from __future__ import annotations

from certificate_app.infrastructure.config.settings import Settings


def test_resolved_frontend_dist_dir_prefers_current_working_directory(
    tmp_path, monkeypatch
) -> None:
    backend_dir = tmp_path / "backend"
    backend_dir.mkdir()
    monkeypatch.chdir(backend_dir)
    dist_dir = tmp_path / "frontend" / "dist"
    dist_dir.mkdir(parents=True)

    settings = Settings(frontend_dist_dir="../frontend/dist")

    assert settings.resolved_frontend_dist_dir == dist_dir.resolve()


def test_resolved_frontend_dist_dir_falls_back_to_repo_root(
    tmp_path, monkeypatch
) -> None:
    backend_dir = tmp_path / "backend"
    backend_dir.mkdir()
    monkeypatch.chdir(backend_dir)
    dist_dir = Settings()._repo_root / "frontend" / "dist"

    settings = Settings(frontend_dist_dir="frontend/dist")

    assert settings.resolved_frontend_dist_dir == dist_dir.resolve()
