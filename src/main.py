from fastapi import FastAPI, APIRouter
import uvicorn, os, sqlite3
from dotenv import load_dotenv

# FastAPI setup
app = FastAPI()

router = APIRouter()

app.include_router(router)

# Carregamento de variáveis .env (ou valores padrão se não houver)
load_dotenv()

API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = int(os.getenv("API_PORT", "8001"))

# Execução da API
if __name__ == "__main__":
    uvicorn.run(app, host=API_HOST, port=API_PORT)
