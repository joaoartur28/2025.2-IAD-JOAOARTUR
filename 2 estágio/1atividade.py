soma = 0
quantidade = 0

while True:
    valor = input("Digite um número: ")

    if valor == "pronto":
        break

    try:
        numero = float(valor)
        soma = soma + numero
        quantidade = quantidade + 1
    except:
        print("Erro, digite um novo número")
        continue

if quantidade > 0:
    media = soma / quantidade
    print("Soma:", soma)
    print("Quantidade:", quantidade)
    print("Média:", media)