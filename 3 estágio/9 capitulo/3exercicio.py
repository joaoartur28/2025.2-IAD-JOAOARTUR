nome_do_arquivo = input("Digite o nome do arquivo: ")
if len(nome_do_arquivo) < 1: 
    nome_do_arquivo = "mbox-short.txt"

try:
    hand = open(nome_do_arquivo)
except FileNotFoundError:
    print(f"O arquivo {nome_do_arquivo} não foi encontrado.")
    exit()

contagem_emails = dict()

for linha in hand:
    if not linha.startswith('From '): 
        continue
    
    palavras = linha.split()
    
    email = palavras[1]
    
    contagem_emails[email] = contagem_emails.get(email, 0) + 1

print("\nHistograma de mensagens por email:")
print(contagem_emails)

hand.close()