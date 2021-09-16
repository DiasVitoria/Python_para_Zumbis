dia = int(input('Insira os dias: '))
hora = int(input('Insira as horas: '))
minu = int(input('Insira os minutos: '))
seg = int(input('Insira os segundos: '))
res = (dia*86400) + (hora*3600) + (minu*60) + seg
print('A soma dos dias, horas, minutos e segundos transformados em segundos é igual a: ', res)
