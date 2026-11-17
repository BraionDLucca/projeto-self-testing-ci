from fastapi import FastAPI
import uvicorn, os
from dotenv import load_dotenv
from controllers.conta_controller import router
from database.conexao import inicializar_banco

# Inicialização do banco SQLite3
inicializar_banco()

# FastAPI setup
app = FastAPI()

app.include_router(router)

# Carregamento de variáveis .env (ou valores padrão se não houver)
load_dotenv()

API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = int(os.getenv("API_PORT", "8001"))

# Execução da API
if __name__ == "__main__":
    uvicorn.run(app, host=API_HOST, port=API_PORT)
