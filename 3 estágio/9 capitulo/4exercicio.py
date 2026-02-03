nome_do_arquivo = input("Digite o nome do arquivo: ")
try:
    manipulador = open(nome_do_arquivo)
except:
    print("Arquivo não pôde ser aberto:", nome_do_arquivo)
    quit()

contagens = dict()

for linha in manipulador:
    palavras = linha.split()
    if len(palavras) < 2 or palavras[0] != 'From':
        continue
    
    email = palavras[1]
    contagens[email] = contagens.get(email, 0) + 1

maior_contagem = None
autor_mais_frequente = None

for email, contagem in contagens.items():
    if maior_contagem is None or contagem > maior_contagem:
        maior_contagem = contagem
        autor_mais_frequente = email

print(autor_mais_frequente, maior_contagem)