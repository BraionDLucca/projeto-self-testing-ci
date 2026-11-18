import pytest
import sqlite3

TEST_DB_URI = "file:capstone_test_db?mode=memory&cache=shared"


def obter_conexao_teste():
    conexao = sqlite3.connect(TEST_DB_URI, uri=True)
    conexao.row_factory = sqlite3.Row
    return conexao


@pytest.fixture
def test_db():
    conexao = obter_conexao_teste()

    conexao.execute("""
        CREATE TABLE contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            saldo REAL NOT NULL,
            limite REAL NOT NULL
        )
    """)

    yield conexao

    conexao.close()
