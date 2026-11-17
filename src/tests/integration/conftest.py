import pytest
import sqlite3


@pytest.fixture
def test_db():
    conexao = sqlite3.connect(":memory:")
    conexao.row_factory = sqlite3.Row

    conexao.execute("""
        CREATE TABLE contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            saldo REAL NOT NULL,
            limite REAL NOT NULL
        )
    """)

    yield conexao

    conexao.close()
