import sys
from pathlib import Path

src = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(src))

from domain.Conta import Conta
import pytest

def test_saldo_insuficiente():
    conta = Conta(80, 500)

    with pytest.raises(ValueError):
        conta.transferir(90, "DEBITO")