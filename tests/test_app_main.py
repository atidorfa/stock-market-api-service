from fastapi.testclient import TestClient
from app.app_main import app


client = TestClient(app)


class TestAppMain:
    def test_app_main_root(self):
        response = client.get('/')
        assert response.status_code == 404

    def test_app_main(self):
        response = client.get('/check')
        assert response.status_code == 200
        assert response.json()['message'] == "OK"
