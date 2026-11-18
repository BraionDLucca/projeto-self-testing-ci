import sqlite3
import pytest
from fastapi.testclient import TestClient
from main import app
from repositories import conta_repository


@pytest.fixture
def client(tmp_path, monkeypatch):
    caminho_banco = tmp_path / "teste.db"

    def obter_conexao_teste():
        conexao = sqlite3.connect(caminho_banco)
        conexao.row_factory = sqlite3.Row
        return conexao

    monkeypatch.setattr(
        conta_repository,
        "obter_conexao",
        obter_conexao_teste
    )

    conexao = obter_conexao_teste()

    conexao.execute("""
        CREATE TABLE contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            saldo REAL NOT NULL,
            limite REAL NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()

    with TestClient(app) as test_client:
        yield test_client


def test_api_funcionando(client):
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert resposta.json() == "API funcionando!"


def test_criar_conta(client):
    resposta = client.post(
        "/contas",
        json={
            "saldo": 100.00,
            "limite": 500.00
        }
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["id"] is not None
    assert dados["saldo"] == 100.00
    assert dados["limite"] == 500.00


def test_buscar_conta_existente(client):
    criacao = client.post(
        "/contas",
        json={
            "saldo": 100.00,
            "limite": 500.00
        }
    )

    id_conta = criacao.json()["id"]

    resposta = client.get(f"/contas/{id_conta}")

    assert resposta.status_code == 200
    assert resposta.json()["id"] == id_conta


def test_buscar_conta_inexistente(client):
    resposta = client.get("/contas/999")

    assert resposta.status_code == 404


def test_transferir_sucesso(client):
    origem = client.post(
        "/contas",
        json={"saldo": 100.00, "limite": 500.00}
    ).json()

    destino = client.post(
        "/contas",
        json={"saldo": 50.00, "limite": 500.00}
    ).json()

    resposta = client.post(
        "/transferir",
        json={
            "id_conta_origem": origem["id"],
            "id_conta_destino": destino["id"],
            "metodo": "DEBITO",
            "valor": 30.00
        }
    )

    assert resposta.status_code == 200


def test_verificar_saldos_apos_transferencia(client):
    origem = client.post(
        "/contas",
        json={"saldo": 100.00, "limite": 500.00}
    ).json()

    destino = client.post(
        "/contas",
        json={"saldo": 50.00, "limite": 500.00}
    ).json()

    client.post(
        "/transferir",
        json={
            "id_conta_origem": origem["id"],
            "id_conta_destino": destino["id"],
            "metodo": "DEBITO",
            "valor": 30.00
        }
    )

    conta_origem = client.get(
        f"/contas/{origem['id']}"
    ).json()

    conta_destino = client.get(
        f"/contas/{destino['id']}"
    ).json()

    assert conta_origem["saldo"] == 70.00
    assert conta_destino["saldo"] == 80.00


def test_transferir_com_saldo_insuficiente(client):
    origem = client.post(
        "/contas",
        json={"saldo": 20.00, "limite": 500.00}
    ).json()

    destino = client.post(
        "/contas",
        json={"saldo": 50.00, "limite": 500.00}
    ).json()

    resposta = client.post(
        "/transferir",
        json={
            "id_conta_origem": origem["id"],
            "id_conta_destino": destino["id"],
            "metodo": "DEBITO",
            "valor": 100.00
        }
    )

    assert resposta.status_code == 400

    conta_origem = client.get(
        f"/contas/{origem['id']}"
    ).json()

    conta_destino = client.get(
        f"/contas/{destino['id']}"
    ).json()

    assert conta_origem["saldo"] == 20.00
    assert conta_destino["saldo"] == 50.00
