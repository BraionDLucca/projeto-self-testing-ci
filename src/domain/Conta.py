class Conta():
    def __init__(self, saldo: float, limite: float):
        self.saldo: float = saldo
        self.limite: float = limite

    def transferir(self, valor: float, metodo: str):

        if metodo == "CREDITO":
            if self.limite - valor < 0:
                raise ValueError("Limite insuficiente.")
            else:
                self.limite = self.limite - valor

        if metodo == "DEBITO":
            if self.saldo - valor < 0:
                raise ValueError("Saldo insuficiente.")
            else:
                self.saldo = self.saldo - valor

    def receber(self, valor: float):
        self.saldo += valor
