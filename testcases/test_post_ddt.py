import pytest
import yaml
from config.settings import get_base_url
from lib.api_client import ApiClient

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

post_data_list = load_yaml("data/post_data.yaml")["test_posts"]

@pytest.mark.parametrize("post_data", post_data_list, ids=lambda x: x["title"])
def test_create_post(post_data):
    client = ApiClient(get_base_url())
    response = client.post("/posts", json=post_data)
    assert response.status_code == 201
    resp_json = response.json()
    assert resp_json["title"] == post_data["title"]
    assert resp_json["body"] == post_data["body"]
    assert resp_json["userId"] == post_data["userId"]
