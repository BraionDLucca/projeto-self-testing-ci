from domain.Conta import Conta
from unittest.mock import patch
from services import conta_service


def test_service_criar_conta_sucesso():
    with patch(
            "services.conta_service.conta_repository"
            ) as conta_repository_mock:

        conta_repository_mock.salvar.return_value = {
            "id": 1,
            "saldo": 80.50,
            "limite": 500.00,
        }

        dados = Conta(80.50, 500.00)

        resultado = conta_service.criar_conta(dados.saldo, dados.limite)

        assert resultado["id"] == 1
        assert resultado["saldo"] == 80.50
        assert resultado["limite"] == 500.00

        conta_repository_mock.salvar.assert_called_once_with(
            {"saldo": 80.50, "limite": 500.00}
        )

# def test_criar_conta_com_saldo_inicial_falha(conta):
#     conta_controller.criar_conta(Conta(0, 0))
