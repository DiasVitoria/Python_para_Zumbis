numTriangular = int(input("Digite o valor do numero triangular: "))
n = 1
while n * (n+1) * (n+2) < numTriangular:
        n = n + 1
if n * (n+1) * (n+2) == numTriangular:
    print(f"{numTriangular} é o produto de {n} * {n + 1} * {n + 2}")
else:
    print(f"{numTriangular} não é triangular")
