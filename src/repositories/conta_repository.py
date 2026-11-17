from database.conexao import obter_conexao


def salvar(conta):
    conexao = obter_conexao()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO contas (saldo, limite) VALUES (?, ?)",
            (conta["saldo"], conta["limite"])
        )

        conexao.commit()

        return conta

    finally:
        conexao.close()


def buscar_por_id(id):
    conexao = obter_conexao()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM contas WHERE id = ?",
            (id)
        )

        return cursor.fetchone()

    finally:
        conexao.close()
