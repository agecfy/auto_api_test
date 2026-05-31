def test_authenticated_request(auth_api_client):
    # 使用已注入 token 的客户端发送请求
    # 这里用 /posts/1 演示，实际应替换为需要认证的接口
    response = auth_api_client.get("/posts/1")
    assert response.status_code == 200
