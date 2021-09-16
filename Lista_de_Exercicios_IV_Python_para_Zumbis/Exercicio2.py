import random
lista = []
par = []
impar = []
for i in range(20):
        n = random.randint(1,100)
        lista.append(n)
        if n%2 == 0:
            par.append(n)
        else:
            impar.append(n)
lista.sort()
print('Lista: ',lista)
print('Par: ',par)
print('Impar: ',impar)


