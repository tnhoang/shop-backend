def test_get_items(client):
    res = client.get("/api/v1/items")
    assert res.status_code == 200
    assert res.json() == "woohoo"