print("----Calculadora para descobrir o maior número----")

valor1 = input("Digite o primeiro valor: ")
valor2 = input("Digite o segundo valor: ")

if valor1 > valor2:
    print("O maior valor é:")
    print(valor1)
elif valor2 < valor1:
    print("O maior valor e:")
    print(valor2)
else:
    print("Ambos os valores são iguais")