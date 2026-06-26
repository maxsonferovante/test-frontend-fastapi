from __future__ import annotations

from fastapi.testclient import TestClient

from certificate_app.main import create_app


def test_frontend_serves_dist_and_spa_fallback(tmp_path, monkeypatch) -> None:
    dist_dir = tmp_path / "dist"
    assets_dir = dist_dir / "assets"
    assets_dir.mkdir(parents=True)
    (dist_dir / "index.html").write_text(
        "<!doctype html><html><body>packaged certificate app</body></html>",
        encoding="utf-8",
    )
    (assets_dir / "app.js").write_text("console.log('packaged');", encoding="utf-8")
    monkeypatch.setenv("FRONTEND_DIST_DIR", str(dist_dir))

    client = TestClient(create_app())

    root_response = client.get("/")
    fallback_response = client.get("/search/certificate")
    asset_response = client.get("/assets/app.js")

    assert root_response.status_code == 200
    assert fallback_response.status_code == 200
    assert asset_response.status_code == 200
    assert "packaged certificate app" in root_response.text
    assert "packaged certificate app" in fallback_response.text
    assert "packaged" in asset_response.text
