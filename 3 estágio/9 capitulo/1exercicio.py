dicionario_de_palavras = dict()

try:
    with open('words.txt', 'r') as arquivo:
        for linha in arquivo:
            palavras = linha.split()
            
            for palavra in palavras:
                palavra_limpa = palavra.lower()
                dicionario_de_palavras[palavra_limpa] = True

    print(f"Dicionário carregado com {len(dicionario_de_palavras)} chaves únicas.")

    termo = input("Digite uma palavra para buscar: ").lower()
    
    if termo in dicionario_de_palavras:
        print(f"A palavra '{termo}' existe no dicionário!")
    else:
        print(f"A palavra '{termo}' NÃO foi encontrada.")

except FileNotFoundError:
    print("Erro")