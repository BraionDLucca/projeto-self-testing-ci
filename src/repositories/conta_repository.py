from main import conexao, cursor

def salvar(conta):
    pass


def buscar_por_id(id):
    cursor.execute("SELECT * FROM contas WHERE id = ?", (id))

    return cursor.fetchone()
