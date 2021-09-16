


primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))
maior = primeiro
menor = primeiro
if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro
if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro
print('Maior: ',maior)
print('Menor: ',menor)


