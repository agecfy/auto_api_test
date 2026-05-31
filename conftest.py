import pytest
from config.settings import get_base_url
from lib.api_client import ApiClient

@pytest.fixture(scope="session")
def api_client():
    """基础客户端，未认证"""
    return ApiClient(get_base_url())

@pytest.fixture(scope="session")
def auth_api_client(api_client):
    """模拟登录，获取 token 并注入"""
    # 注意：以下为模拟演示，实际使用时替换为真实的登录接口调用
    # 这里我们直接设置一个假的 token 来演示依赖处理模式
    fake_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlRlc3RVc2VyIiwiaWF0IjoxNTE2MjM5MDIyfQ"
    api_client.set_token(fake_token)
    return api_client
