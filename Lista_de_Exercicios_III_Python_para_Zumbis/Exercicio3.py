paisA = 80000
paisB = 200000
taxaA = 3/100
taxaB = 1.5/100
ano = 0
while paisA<paisB:
    paisA += paisA*taxaA
    paisB += paisB*taxaB
    ano += 1
print(f'Serão necessarios {ano} anos para que o pais A alcance o pais B')


