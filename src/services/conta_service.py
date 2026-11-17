from repositories import conta_repository


def criar_conta(saldo: float, limite: float):
    if saldo <= 0:
        raise ValueError(
            "Contas precisam de saldo acima de 0 (zero) para serem criadas."
            )

    if limite < 0:
        raise ValueError("Limite não pode ser negativo.")

    conta = {"saldo": saldo, "limite": limite}

    return conta_repository.salvar(conta)


def transferir(id_conta_origem, id_conta_destino, metodo, valor):
    pass
