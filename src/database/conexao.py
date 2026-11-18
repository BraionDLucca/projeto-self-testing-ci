import sqlite3


def obter_conexao():
    conexao = sqlite3.connect("database/banco.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar_banco():
    conexao = obter_conexao()

    try:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS contas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                saldo REAL NOT NULL,
                limite REAL NOT NULL
            )
        """)

        conexao.commit()

    finally:
        conexao.close()
