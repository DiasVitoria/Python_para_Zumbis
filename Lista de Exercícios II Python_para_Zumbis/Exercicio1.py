A=float(input("Informe o primeiro valor do lado do triângulo: "))
B=float(input("Informe o segundo valor do lado do triângulo: "))
C=float(input("Informe o terceiro valor do lado do triângulo: "))
if A<B+C and B<A+C and C<B+A:
    if A==B and B==C:
        print("Equilátero")
    elif A!=B and B!=C and C!=A:
        print("Escaleno")
    else:
        print("Isósceles")
else:
        print("Os valores inseridos não formam um triângulo")
