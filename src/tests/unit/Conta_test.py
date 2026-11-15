import sys
from pathlib import Path

src = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(src))

from domain.Conta import Conta
import pytest

@pytest.fixture
def conta():
    return Conta(80, 500)

@pytest.mark.parametrize("valor", [(79.99), (80.00)])
def test_transferencia_debito_sucesso(conta, valor):
    saldo_antes = conta.saldo
    conta.transferir(valor, "DEBITO")
    assert conta.saldo == saldo_antes - valor

def test_transferencia_debito_falha(conta):
    with pytest.raises(ValueError):
        conta.transferir(80.01, "DEBITO")

@pytest.mark.parametrize("valor", [(499.99), (500.00)])
def test_transferencia_credito_sucesso(conta, valor):
    limite_antes = conta.limite
    conta.transferir(valor, "CREDITO")
    assert conta.limite == limite_antes - valor

def test_transferencia_credito_falha(conta):
    with pytest.raises(ValueError):
        conta.transferir(500.01, "CREDITO")