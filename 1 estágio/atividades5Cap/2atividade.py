entrada = input("Digite os números separados por espaço: ")

numeros = []
for item in entrada.split():
    try:
        numeros.append(float(item))
    except:
        print(f"Ignorando valor inválido: {item}")

if numeros:
    print("\nResultados:")
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")
else:
    print("Nenhum número válido foi digitado.")
