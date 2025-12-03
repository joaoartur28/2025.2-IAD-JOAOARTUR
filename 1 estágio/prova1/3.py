salario = float(input("Digite o seu salário: "))

if salario < 500:
    valor_1 = salario * 1.15
    print(valor_1)
elif salario >1000:
    valor_2 = salario * 1.05
    print(valor_2)
else:
    valor_3 = salario * 1.10
    print(valor_3)
