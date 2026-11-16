from unittest.mock import patch
from src.controllers.conta_controller import criar_conta

def test_criar_conta_sucesso():
    with patch(
        "src.controllers.conta_controller.conta_service"
    ) as conta_service_mock:

        conta_service_mock.criar_conta.return_value = {
            "id": 1,
            "saldo": 80.50,
            "limite": 500.00
        }

        resultado = criar_conta(80.50, 500.00)

        assert resultado["id"] == 1
        assert resultado["saldo"] == 80.50
        assert resultado["limite"] == 500.00

        conta_service_mock.criar_conta.assert_called_once_with(
            80.50, 500.00
        )