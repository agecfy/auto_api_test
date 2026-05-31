from config.settings import get_base_url
from lib.api_client import ApiClient

def test_get_post():
    client = ApiClient(get_base_url())
    response = client.get("/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
