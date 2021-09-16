
metros=int(input('informe o valor em metros a serem pintados: '))
tintas = int(metros/54)
resto = metros%54
if resto > 0:
    tintas=tintas+1
valor = tintas * 80
print('valor a pagar: R$',valor)
print('Quantidades necessárias: ',tintas)
