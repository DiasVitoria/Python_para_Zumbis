valorDaConta = int(input("Valor total da conta: "))
valorDoPagamento = int(input("Pagamento efetuado de: "))
caixa = [50, 20, 10, 5, 2, 1]
troco = valorDoPagamento - valorDaConta
for notas in caixa:
    if troco >= notas:
        quantidade = troco / notas
        r = troco - (notas * int(quantidade))
        print(int(quantidade),"notas de R$",notas)
        troco = r
