class Conta():
    def __init__(self, saldo: float, limite: float):
        self.saldo: float = saldo
        self.limite: float = limite

    def transferir(self, valor: float, metodo: str):

        if metodo == "CREDITO":
            if valor > self.limite:
                raise ValueError("Limite insuficiente.")
            else:
                self.limite = self.limite - valor

        if metodo == "DEBITO":
            if valor > self.saldo:
                raise ValueError("Saldo insuficiente.")
            else:
                self.saldo = self.saldo - valor

    def receber(self, valor: float):
        self.saldo += valor
