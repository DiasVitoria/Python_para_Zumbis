salario = float(input('Insira o valor do seu salário atual: '))
porc = int(input('Insira o valor da porcentagem: %'))
porcres = porc / 100
calcporc = salario * porcres
salfinal = salario + calcporc
print('Seu aumento será de: ', calcporc, 'O valor total de seu salário será de: ',salfinal)
