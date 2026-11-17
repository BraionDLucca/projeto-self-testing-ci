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

        return {
            "id": cursor.lastrowid,
            **conta
            }

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


def salvar_transferencia(conta_origem, conta_destino):
    pass
