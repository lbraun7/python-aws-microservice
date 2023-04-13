from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki, search_wiki, phrases

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "Wikipedia API"}

@app.get("/search/{value}")
async def search(value: str):
    
    result = search_wiki(value)
    
    return{"results": result}

@app.get("/wiki/{name}")
async def wiki(name: str):
    
    result = wiki(name)
    
    return{"results": result}

@app.get("/phrase/{name}")
async def phrase(name: str):
    
    result = phrases(name)
    
    return{"results": result}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
    
