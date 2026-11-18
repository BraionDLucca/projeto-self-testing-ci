import os
import sqlite3


def obter_conexao():
    # Caminho do banco de dados
    db_path = "database/banco.db"

    # Extrai o diretório ("database") e o cria se não existir
    db_dir = os.path.dirname(db_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)

    conexao = sqlite3.connect(db_path)
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
