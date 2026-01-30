nomedoarquivo = input("Digite o nome do arquivo: ")

try:
    arquivo = open(nomedoarquivo)
except:
    print("arquivo não encontrado")

contador = 0

for linha in arquivo:
    if linha.startswith("From "):
        palavras = linha.split()
        print(palavras[1])
        contador = contador + 1

arquivo.close()

print(contador, "contas enviaram email para o individuo.")
