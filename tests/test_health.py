from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from madr_mcp_server.app import create_app


def test_health():
    app = create_app()
    with app.test_client() as client:
        response = client.get('/health')
        assert response.status_code == 200
        assert response.get_json() == {'status': 'ok'}
