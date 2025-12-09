texto = input("digite o nome de um arquivo: ")

try:
    arquivo = open(texto)
except:
    print("arquivo não encontrado")
    quit()

for linha in arquivo:
    linha = linha.rstrip()
    print(linha.upper())