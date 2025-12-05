# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os 
from modules import tools
from dotenv import load_dotenv 

load_dotenv()

API_ROOT_URL =  f"http://127.0.0.1:{os.getenv('FASTAPI_PORT', '8080')}"
                                    

# models pydantic
class QuoteRequest(BaseModel):
    id : int
    text : str

class QuoteResponse(BaseModel):
    text : str

# --- Configuration ---
app = FastAPI(title="API")

# --- Routes API ---
# http://www.google.com/fr route fr
# http://www.google.com/en route en 
# http://www.google.com/ route principale

@app.get("/")
def read_root():
    return {"Hello": "World", "status": "API is running"}


@app.post("/insert/")
def insert_quote(quote: QuoteRequest):

@app.get("/read/", response_model=list[QuoteResponse])
def read_all():
    db = tools.read_db()
    return db.to_json()








if __name__ == "__main__":
    # 1 - on récupère le port de l'API
    try:
        print("Hello")
        port = os.getenv('FAST_API_PORT')
        url = os.getenv('API_BASE_URL')
        port = int(port)
        print(port)
    except ValueError:
        print("ERREUR")
        port = 8080

    # 2 - On lance uvicorn
    uvicorn.run(
        "main:app", 
        host = url,
        port = port, 
        reload = True
    )