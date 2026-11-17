from domain.Conta import Conta
from unittest.mock import patch, call
from services import conta_service
import pytest


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


@pytest.mark.parametrize("saldo", [(0), (-0.01)])
def test_service_criar_conta_falha_saldo(saldo):
    dados = Conta(saldo, 500.00)

    with pytest.raises(ValueError):
        conta_service.criar_conta(dados.saldo, dados.limite)


def test_service_criar_conta_falha_limite():
    dados = Conta(50, -0.01)

    with pytest.raises(ValueError):
        conta_service.criar_conta(dados.saldo, dados.limite)


def test_buscar_por_id_sucesso():
    with patch(
        "services.conta_service.conta_repository"
    ) as conta_repository_mock:

        conta_repository_mock.buscar_por_id.return_value = (
            1, 80.50, 500.00
        )

        resultado = conta_service.buscar_por_id(1)

        assert resultado["id"] == 1
        assert resultado["saldo"] == 80.50
        assert resultado["limite"] == 500.00

        conta_repository_mock.buscar_por_id.assert_called_once_with(1)


def test_buscar_por_id_conta_nao_encontrada():
    with patch(
        "services.conta_service.conta_repository"
    ) as conta_repository_mock:

        conta_repository_mock.buscar_por_id.return_value = None

        with pytest.raises(ValueError) as erro:
            conta_service.buscar_por_id(999)

        assert str(erro.value) == "Conta não encontrada."

        conta_repository_mock.buscar_por_id.assert_called_once_with(999)


@pytest.mark.parametrize(("valor"), [(10), (5)])
def test_service_transferencia_debito_sucesso(valor):
    conta_origem = Conta(100.00, 500.00)
    conta_destino = Conta(200.00, 1000.00)

    with patch(
        "services.conta_service.conta_repository"
    ) as conta_repository_mock:

        conta_repository_mock.buscar_por_id.side_effect = [
            {
                "id": 1,
                "saldo": conta_origem.saldo,
                "limite": conta_origem.limite
            },
            {
                "id": 2,
                "saldo": conta_destino.saldo,
                "limite": conta_destino.limite
            }
        ]

        resultado = conta_service.transferir(1, 2, "DEBITO", valor)

        conta_repository_mock.buscar_por_id.assert_has_calls([
            call(1),
            call(2)
        ])

        conta_repository_mock.salvar_transferencia.assert_called_once()

        assert resultado == conta_repository_mock.salvar_transferencia.return_value

        id_origem, conta_salva_origem, id_destino, conta_salva_destino = (
            conta_repository_mock.salvar_transferencia.call_args.args
        )

        assert id_origem == 1
        assert id_destino == 2

        assert conta_salva_origem.saldo == 100.00 - valor
        assert conta_salva_origem.limite == 500.00

        assert conta_salva_destino.saldo == 200.00 + valor
        assert conta_salva_destino.limite == 1000.00


@pytest.mark.parametrize(("valor"), [(10), (5)])
def test_service_transferencia_credito_sucesso(valor):
    conta_origem = Conta(100.00, 500.00)
    conta_destino = Conta(200.00, 1000.00)

    with patch(
        "services.conta_service.conta_repository"
    ) as conta_repository_mock:

        conta_repository_mock.buscar_por_id.side_effect = [
            {
                "id": 1,
                "saldo": conta_origem.saldo,
                "limite": conta_origem.limite
            },
            {
                "id": 2,
                "saldo": conta_destino.saldo,
                "limite": conta_destino.limite
            }
        ]

        resultado = conta_service.transferir(1, 2, "CREDITO", valor)

        conta_repository_mock.buscar_por_id.assert_has_calls([
            call(1),
            call(2)
        ])

        conta_repository_mock.salvar_transferencia.assert_called_once()

        assert resultado == conta_repository_mock.salvar_transferencia.return_value

        id_origem, conta_salva_origem, id_destino, conta_salva_destino = (
            conta_repository_mock.salvar_transferencia.call_args.args
        )

        assert id_origem == 1
        assert id_destino == 2

        assert conta_salva_origem.saldo == 100.00 
        assert conta_salva_origem.limite == 500.00 - valor

        assert conta_salva_destino.saldo == 200.00 + valor
        assert conta_salva_destino.limite == 1000.00
