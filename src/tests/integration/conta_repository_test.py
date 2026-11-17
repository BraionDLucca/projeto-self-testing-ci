from unittest.mock import patch
from repositories import conta_repository


def test_buscar_por_id():
    resultado_esperado = {
        "id": 1,
        "saldo": 80.50,
        "limite": 500.00
    }

    with patch(
        "repositories.conta_repository.cursor"
    ) as cursor_mock:

        cursor_mock.fetchone.return_value = resultado_esperado

        resultado = conta_repository.buscar_por_id(1)

        assert resultado == resultado_esperado

        cursor_mock.execute.assert_called_once_with(
            "SELECT * FROM contas WHERE id = ?",
            (1)
        )