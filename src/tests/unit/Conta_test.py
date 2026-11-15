def test_saldo_negativo():
    conta = Conta(80, 500)

    conta.transferir(90, "DEBITO")
    assert conta.saldo == 80