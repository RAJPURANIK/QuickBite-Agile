from app import app

def test_home_page_loads():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"QuickBite" in response.data

def test_search_food():
    client = app.test_client()
    response = client.get("/?q=Paneer")
    assert response.status_code == 200
    assert b"Paneer Tikka Wrap" in response.data
    assert b"Chicken Rice Bowl" not in response.data

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"
