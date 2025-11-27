while True:
    valor = input("digite um valor:")
    if valor == "pronto":
        break

    try:
        float(valor)
    except:
        print("Entrada inválida, digite um valor numérico")
