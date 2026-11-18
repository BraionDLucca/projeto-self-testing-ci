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
            (id,)
        )

        return cursor.fetchone()

    finally:
        conexao.close()


def salvar_transferencia(
            id_conta_origem,
            conta_origem,
            id_conta_destino,
            conta_destino
        ):
    conexao = obter_conexao()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            "UPDATE contas SET (saldo, limite) = (?, ?) WHERE id = ?",
            (conta_origem.get_saldo(), conta_origem.get_limite(), id_conta_origem)
        )

        cursor.execute(
            "UPDATE contas SET (saldo, limite) = (?, ?) WHERE id = ?",
            (conta_destino.get_saldo(), conta_destino.get_limite(), id_conta_destino)
        )

        conexao.commit()

        conta_origem_salva = buscar_por_id(id_conta_origem)
        conta_destino_salva = buscar_por_id(id_conta_destino)

        return {
            "conta_origem": conta_origem_salva,
            "conta_destino": conta_destino_salva,
        }

    finally:
        conexao.close()
