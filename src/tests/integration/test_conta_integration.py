import pytest
from unittest.mock import patch
from services import conta_service
from conftest import obter_conexao_teste


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


def test_criar_conta_e_verificar_no_banco(test_db):
    with patch(
        "repositories.conta_repository.obter_conexao",
        side_effect=obter_conexao_teste
    ):
        conta_service.criar_conta(80.50, 500.00)

    cursor = test_db.execute(
        "SELECT * FROM contas WHERE id = 1"
    )

    resultado = cursor.fetchone()

    assert resultado["id"] == 1
    assert resultado["saldo"] == 80.50
    assert resultado["limite"] == 500.00


def test_transferir_e_verificar_no_banco(test_db):
    with patch(
        "repositories.conta_repository.obter_conexao",
        side_effect=obter_conexao_teste
    ):
        conta_service.criar_conta(100.00, 500.00)
        conta_service.criar_conta(50.00, 500.00)

        conta_service.transferir(1, 2, "DEBITO", 30.00)

    cursor = test_db.execute(
        "SELECT * FROM contas ORDER BY id"
    )

    contas = cursor.fetchall()

    assert contas[0]["saldo"] == 70.00
    assert contas[1]["saldo"] == 80.00


def test_transferir_saldo_insuficiente_sem_alterar_banco(test_db):
    with patch(
        "repositories.conta_repository.obter_conexao",
        side_effect=obter_conexao_teste
    ):
        conta_service.criar_conta(20.00, 500.00)
        conta_service.criar_conta(50.00, 500.00)

        with pytest.raises(ValueError) as erro:
            conta_service.transferir(1, 2, "DEBITO", 100.00)

    assert str(erro.value) == "Saldo insuficiente."

    cursor = test_db.execute(
        "SELECT * FROM contas ORDER BY id"
    )
    contas = cursor.fetchall()

    assert contas[0]["saldo"] == 20.00
    assert contas[1]["saldo"] == 50.00


def test_transferir_para_mesma_conta(test_db):
    with patch(
        "repositories.conta_repository.obter_conexao",
        side_effect=obter_conexao_teste
    ):
        conta_service.criar_conta(100.00, 500.00)

        with pytest.raises(ValueError) as erro:
            conta_service.transferir(1, 1, "DEBITO", 30.00)

    assert str(erro.value) == (
        "Transferências não podem ser feitas para a mesma conta."
    )

    cursor = test_db.execute(
        "SELECT saldo FROM contas WHERE id = 1"
    )

    assert cursor.fetchone()["saldo"] == 100.00
