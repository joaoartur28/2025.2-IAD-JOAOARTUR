try:
    pontuaçao = float(input("digite a Pontuação:"))
except:
    print("pontuação inválida")
if pontuaçao < 0.0:
    print("pontuação inválida")
elif pontuaçao > 1.0:
    print("pontuação inválida")
elif pontuaçao >= 0.9:
    print("A")
elif pontuaçao >=0.8:
    print("B")
elif pontuaçao >= 0.7:
    print("C")
elif pontuaçao >=0.6:
    print("D")
elif pontuaçao < 0.6:
    print("F")