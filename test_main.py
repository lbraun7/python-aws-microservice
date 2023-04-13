from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API"}
    
def test_read_phrase():
    response = client.get("/phrase/SteveJobs")
    assert response.status_code == 200
    assert response.json() == { 
        "results": [
            "steven paul jobs",
            "february",
            "october",
            "american business magnate",
            "industrial designer",
            "media proprietor"
        ]}    
    
