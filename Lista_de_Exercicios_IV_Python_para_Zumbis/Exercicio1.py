import random
lista = []
maior = 0
menor = 100
for i in range(10):
	n = random.randint(1,100)
	lista.append(n)
	if n < menor: 
		menor = n
	if n > maior:
		maior = n
lista.sort()
print (lista)
print('Menor: ', menor)
print('Maior: ', maior)


