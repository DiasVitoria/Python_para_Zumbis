
km = int(input("Informe a distância em km/h percorridas: "))
diasAlugados = int(input("Informe os dias alugados: "))
precoTotal = (diasAlugados * 60) + (km * 0.15)
print("O total a pagar será de: R$",precoTotal)
