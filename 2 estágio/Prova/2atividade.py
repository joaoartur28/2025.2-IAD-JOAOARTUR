numeros = []

while True:
    entrada = input("Digite um número: ")

    if entrada == "pronto":
        break

    try:
        numero = float(entrada)
        numeros.append(numero)
    except:
        print("Entrada inválida")

if len(numeros) > 0:
    print("Máximo:", max(numeros))
    print("Mínimo:", min(numeros))

