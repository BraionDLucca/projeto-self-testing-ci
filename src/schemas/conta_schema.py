from pydantic import BaseModel


class CriarContaRequest(BaseModel):
    saldo: float
    limite: float


class TransferenciaRequest(BaseModel):
    id_conta_origem: int
    id_conta_destino: int
    metodo: str
    valor: float
