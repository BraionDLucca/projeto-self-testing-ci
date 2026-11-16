from fastapi import HTTPException
from services.conta_service import ContaService
from schemas.conta_schema import CriarContaRequest

conta_service = ContaService()


def criar_conta(dados: CriarContaRequest):
    try:
        return conta_service.criar_conta(dados.saldo, dados.limite)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))
