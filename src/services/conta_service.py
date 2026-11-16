from repositories import conta_repository


def criar_conta(saldo: float, limite: float):
    if saldo <= 0:
        raise ValueError(
            "Contas precisam de saldo acima de 0 (zero) para serem criadas."
            )

    conta = {"saldo": saldo, "limite": limite}

    return conta_repository.salvar(conta)
