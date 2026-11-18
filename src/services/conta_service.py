from repositories import conta_repository
from domain.Conta import Conta


def criar_conta(saldo: float, limite: float):
    if saldo <= 0:
        raise ValueError(
            "Contas precisam de saldo acima de 0 (zero) para serem criadas."
            )

    if limite < 0:
        raise ValueError("Limite não pode ser negativo.")

    conta = {"saldo": saldo, "limite": limite}

    return conta_repository.salvar(conta)


def buscar_por_id(id):
    conta = conta_repository.buscar_por_id(id)

    if conta is None:
        raise ValueError("Conta não encontrada.")

    return {
        "id": conta[0],
        "saldo": conta[1],
        "limite": conta[2]
    }


def transferir(id_conta_origem, id_conta_destino, metodo, valor):

    if id_conta_origem == id_conta_destino:
        raise ValueError(
            "Transferências não podem ser feitas para a mesma conta."
            )

    if valor <= 0:
        raise ValueError(
            "Valor de transferência deve ser acima de 0 (zero)."
            )

    dados_conta_origem = conta_repository.buscar_por_id(id_conta_origem)

    dados_conta_destino = conta_repository.buscar_por_id(id_conta_destino)

    conta_origem = Conta(dados_conta_origem[1], dados_conta_origem[2])

    conta_destino = Conta(dados_conta_destino[1], dados_conta_destino[2])

    conta_origem.transferir(valor, metodo)

    conta_destino.receber(valor)

    return conta_repository.salvar_transferencia(
        id_conta_origem, conta_origem, id_conta_destino, conta_destino
        )
