import pytest
from unittest.mock import patch
from services import conta_service


def test_buscar_por_id_sucesso(test_db):
    test_db.execute("""
        INSERT INTO contas (saldo, limite)
        VALUES (80.50, 500.00)
    """)
    test_db.commit()

    with patch(
        "repositories.conta_repository.obter_conexao",
        return_value=test_db
    ):
        resultado = conta_service.buscar_por_id(1)

    assert resultado["id"] == 1
    assert resultado["saldo"] == 80.50
    assert resultado["limite"] == 500.00


def test_buscar_por_id_conta_nao_encontrada(test_db):
    with patch(
        "repositories.conta_repository.obter_conexao",
        return_value=test_db
    ):
        with pytest.raises(ValueError) as erro:
            conta_service.buscar_por_id(999)

    assert str(erro.value) == "Conta não encontrada."
