def computarNotas(pontuacao):
    if pontuacao >= 0.9:
        return "A"
    elif pontuacao >= 0.8:
        return "B"
    elif pontuacao >= 0.7:
        return "C"
    elif pontuacao >= 0.6:
        return "D"
    else:
        return "F"

try:
    p = float(input("Digite a pontuação (0 a 1): "))

    if p < 0 or p > 1:
        print("Erro: a pontuação deve estar entre 0 e 1.")
    else:
        nota = computarNotas(p)
        print("Nota:", nota)

except ValueError:
    print("Entrada inválida! Digite um número.")
