from collections import Counter

def contar_frequencias(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read().lower()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return

    contador = Counter()

    for caractere in texto:
        if 'a' <= caractere <= 'z':
            contador[caractere] += 1

    frequencias_ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    print("\nFrequência de letras (ordem decrescente):\n")
    for letra, freq in frequencias_ordenadas:
        print(f"{letra}: {freq}")


nome_arquivo = input("Digite o nome do arquivo de texto: ")
contar_frequencias(nome_arquivo)
