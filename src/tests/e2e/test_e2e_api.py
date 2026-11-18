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
