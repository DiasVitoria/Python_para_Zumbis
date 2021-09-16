

salarioBruto=float(input("Informe seu salário bruto: "))
IR=salarioBruto*(11/100)
INSS=salarioBruto*(8/100)
SIND=salarioBruto*(5/100)
salarioLiq=salarioBruto-IR-INSS-SIND
print(
    ' Sindicato: R$-',SIND,'\n',
    'INSS: R$-',INSS,'\n',
    'Imposto: R$-',IR,'\n',
    'seu salario é de: R$',salarioLiq)

