soma = 0
quantidade = 0

while True:
    valor = input("digite um valor: ")

    if valor == "pronto":
        break

    try:
        numero = float(valor)
        soma = soma + numero
        quantidade = quantidade + 1
    except:
        print("Entrada inválida, digite um valor numérico")
        continue
