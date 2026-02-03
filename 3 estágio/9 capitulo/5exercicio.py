nome_do_arquivo = input("Digite o nome do arquivo: ")
try:
    manipulador = open(nome_do_arquivo)
except:
    print("Arquivo não pôde ser aberto:", nome_do_arquivo)
    quit()

contagens_dominio = dict()

for linha in manipulador:
    palavras = linha.split()
    
    if len(palavras) < 2 or palavras[0] != 'From':
        continue
    
    email = palavras[1]
    
    partes_email = email.split('@')
    if len(partes_email) > 1:
        dominio = partes_email[1]
        
        contagens_dominio[dominio] = contagens_dominio.get(dominio, 0) + 1

print(contagens_dominio)