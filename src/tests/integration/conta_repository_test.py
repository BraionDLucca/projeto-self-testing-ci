from unittest.mock import patch
from repositories import conta_repository


def test_repository_salvar():
    
    conta = {
        "saldo": 80.50,
        "limite": 500.00
        }

    with patch(
        "repositories.conta_repository.obter_conexao"
    ) as conexao_mock:

        resultado = conta_repository.salvar(conta)

        assert resultado == conta

        conexao_mock.return_value.cursor.return_value.execute.assert_called_once_with(
            "INSERT INTO contas (saldo, limite) VALUES (?, ?)",
            (conta["saldo"], conta["limite"])
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

        conexao_mock.return_value.cursor.return_value.fetchone.return_value = resultado_esperado

        resultado = conta_repository.buscar_por_id(1)

        assert resultado == resultado_esperado

        conexao_mock.return_value.cursor.return_value.execute.assert_called_once_with(
            "SELECT * FROM contas WHERE id = ?",
            (1)
        )

        conexao_mock.return_value.cursor.return_value.fetchone.assert_called_once()

        conexao_mock.return_value.close.assert_called_once()
