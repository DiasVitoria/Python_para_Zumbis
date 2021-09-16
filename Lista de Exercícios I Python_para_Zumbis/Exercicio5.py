
prod = float(input("Informe o valor total da compra: "))
desc = float(input("Informe a porcentagem do desconto: "))
porcprod = desc / 100
valordesc = prod * porcprod
valortotal = prod - valordesc
print('Valor total a pagar: ',valortotal)
