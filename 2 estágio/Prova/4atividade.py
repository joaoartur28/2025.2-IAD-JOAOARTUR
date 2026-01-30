nomedoarquivo = input("Digite o nome do arquivo: ")
arquivo = open(nomedoarquivo)

palavrasunicas = []

for linha in arquivo:
    palavras = linha.split()
    for palavra in palavras:
        if palavra not in palavrasunicas:
            palavrasunicas.append(palavra)

palavrasunicas.sort()
print(palavrasunicas)