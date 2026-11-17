from fastapi import HTTPException
from services import conta_service
from schemas.conta_schema import CriarContaRequest
from main import router


@router.get("/")
def home():
    return "API funcionando na porta 8000!"


@router.post("/contas")
def criar_conta(dados: CriarContaRequest):
    try:
        return conta_service.criar_conta(dados.saldo, dados.limite)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))
