fruta = input("qual é a fruta? ")

indice = len(fruta)
while indice > 0:
    letra = fruta[indice - 1]
    print(letra)
    indice = indice - 1