nome_arquivo = input("Digite o nome do arquivo: ")
fhand = open(nome_arquivo)

palavras_unicas = []

for linha in fhand:
    palavras = linha.split()
    for palavra in palavras:
        if palavra not in palavras_unicas:
            palavras_unicas.append(palavra)

palavras_unicas.sort()
print(palavras_unicas)
