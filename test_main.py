from fastapi import FastAPI
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
    
def test_read_search():
    response = client.get("/search/Steve")
    assert response.status_code == 200
    assert response.json() == { 
        "results": [
            "STEVE",
            "Steve",
            "Steve Jobs",
            "Steve Buscemi",
            "Steve Carell",
            "Steve Harvey",
            "Steve Wood",
            "Steve Roach",
            "Steve McQueen",
            "Stone Cold Steve Austin"
        ]}           