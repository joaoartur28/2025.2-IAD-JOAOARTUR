nomedoarquivo = input("Digite o nome de um arquivo: ")

try:
    arquivo = open(nomedoarquivo)
except:
    print("Arquivo não encontrado.")

contagem = 0

for linha in arquivo:
    if linha.startswith("X-DSPAM-Confidence:"):
        contagem = contagem + 1
        print(contagem)