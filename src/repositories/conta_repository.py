from database.conexao import obter_conexao

def salvar(conta):
    pass


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
