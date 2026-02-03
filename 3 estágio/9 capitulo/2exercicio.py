nome_do_arquivo = input("Digite o nome do arquivo: ")

try:
    fhand = open(nome_do_arquivo)
except FileNotFoundError:
    print(f"Arquivo não encontrado: {nome_do_arquivo}")
    exit()

contagem_dias = dict()

for linha in fhand:
    if not linha.startswith('From '):
        continue
    
    palavras = linha.split()
    
    if len(palavras) > 2:
        dia = palavras[2]
        contagem_dias[dia] = contagem_dias.get(dia, 0) + 1

fhand.close()

print(contagem_dias)