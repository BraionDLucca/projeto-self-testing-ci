from unittest.mock import patch
from controllers import conta_controller
from schemas.conta_schema import CriarContaRequest, TransferenciaRequest
import pytest
from fastapi import HTTPException


def test_controller_criar_conta_sucesso():
    with patch(
        "controllers.conta_controller.conta_service"
    ) as conta_service_mock:

        conta_service_mock.criar_conta.return_value = {
            "id": 1,
            "saldo": 80.50,
            "limite": 500.00
        }

        dados = CriarContaRequest(saldo=80.50, limite=500.00)

        resultado = conta_controller.criar_conta(dados)

        assert resultado["id"] == 1
        assert resultado["saldo"] == 80.50
        assert resultado["limite"] == 500.00

        conta_service_mock.criar_conta.assert_called_once_with(
            80.50, 500.00
        )


def test_controller_transferencia_sucesso():
    with patch(
        "controllers.conta_controller.conta_service"
    ) as conta_service_mock:

        conta_service_mock.transferir.return_value = {
            "id_conta_origem": 1,
            "id_conta_destino": 2,
            "metodo":"DEBITO",
            "valor": 500.00
        }

        dados = TransferenciaRequest(
                    id_conta_origem=1,
                    id_conta_destino=2,
                    metodo="DEBITO",
                    valor=500.00
                    )

        resultado = conta_controller.transferir(dados)

        assert resultado["id_conta_origem"] == 1
        assert resultado["id_conta_destino"] == 2
        assert resultado["metodo"] == "DEBITO"
        assert resultado["valor"] == 500.00

        conta_service_mock.transferir.assert_called_once_with(
            1, 2, "DEBITO", 500.00
        )

def test_controller_buscar_conta_por_id_sucesso():
    with patch(
        "controllers.conta_controller.conta_service"
    ) as conta_service_mock:

        conta_service_mock.buscar_por_id.return_value = {
            "id": 1,
            "saldo": 80.50,
            "limite": 500.00
        }

        resultado = conta_controller.buscar_conta_por_id(1)

        assert resultado["id"] == 1
        assert resultado["saldo"] == 80.50
        assert resultado["limite"] == 500.00

        conta_service_mock.buscar_por_id.assert_called_once_with(1)
