from unittest.mock import patch, call
from repositories import conta_repository
from domain.Conta import Conta


def test_repository_salvar():

    resultado_esperado = {
        "id": 1,
        "saldo": 80.50,
        "limite": 500.00
        }

    with patch(
        "repositories.conta_repository.obter_conexao"
    ) as conexao_mock:
        
        conexao_mock.return_value.cursor.return_value.lastrowid = 1
        
        resultado = conta_repository.salvar(resultado_esperado)      

        assert resultado == resultado_esperado

        conexao_mock.return_value.cursor.return_value.execute.assert_called_once_with(
            "INSERT INTO contas (saldo, limite) VALUES (?, ?)",
            (resultado_esperado["saldo"], resultado_esperado["limite"])
        )

        conexao_mock.return_value.commit.assert_called_once()      

        conexao_mock.return_value.close.assert_called_once()


def test_buscar_por_id():
    resultado_esperado = {
        "id": 1,
        "saldo": 80.50,
        "limite": 500.00
    }

    with patch(
        "repositories.conta_repository.obter_conexao"
    ) as conexao_mock:

        conexao_mock.return_value.cursor.return_value.fetchone.return_value = (
            resultado_esperado
            )

        resultado = conta_repository.buscar_por_id(1,)

        assert resultado == resultado_esperado

        conexao_mock.return_value.cursor.return_value.execute.assert_called_once_with(
            "SELECT * FROM contas WHERE id = ?",
            (1,)
        )

        conexao_mock.return_value.cursor.return_value.fetchone.assert_called_once()

        conexao_mock.return_value.close.assert_called_once()


def test_repository_salvar_transferencia():

    resultado_esperado = {
        "conta_origem": {"id": 1, "saldo": 80.50, "limite": 500.00},
        "conta_destino": {"id": 2, "saldo": 150.00, "limite": 300.00}
    }

    conta_origem = Conta(80.50, 500.00)
    conta_destino = Conta(150.00, 300.00)

    with patch(
        "repositories.conta_repository.obter_conexao"
    ) as conexao_mock, patch(
        "repositories.conta_repository.buscar_por_id",
        side_effect=[
            resultado_esperado["conta_origem"],
            resultado_esperado["conta_destino"]
        ]
    ) as buscar_mock, patch.object(
        conta_origem, "get_saldo", return_value=80.50
    ), patch.object(
        conta_origem, "get_limite", return_value=500.00
    ), patch.object(
        conta_destino, "get_saldo", return_value=150.00
    ), patch.object(
        conta_destino, "get_limite", return_value=300.00
    ):

        resultado = conta_repository.salvar_transferencia(
            1, conta_origem, 2, conta_destino
        )

        assert resultado == resultado_esperado

        cursor_mock = conexao_mock.return_value.cursor.return_value

        assert cursor_mock.execute.call_count == 2

        buscar_mock.assert_has_calls([
            call(1),
            call(2)
        ])

        conexao_mock.return_value.commit.assert_called_once()
        conexao_mock.return_value.close.assert_called_once()
