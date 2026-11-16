from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import os
from controllers.conta_controller import router

app = FastAPI()

app.include_router(router)

load_dotenv()

API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = int(os.getenv("API_PORT", "8001"))

if __name__ == "__main__":
    uvicorn.run(app, host=API_HOST, port=API_PORT)
