from pydantic import BaseModel


class CriarContaRequest(BaseModel):
    saldo: float
    limite: float
