funcionário = input("você é funcionário? ")
try:
    hora = float(input("digite as horas: "))
except:
    print("erro, por favor utilize uma entrada numérica")
try:
    taxa = float(input("digite a taxa: "))
except:
    print("erro, por favor utilize uma entrada numérica")
if funcionário == "não":
    valor1 = hora * taxa
    print(valor1)
elif funcionário == "sim":
    if hora >= 40:
        valor_taxa = ((hora - 40) * taxa * 1.5)
        valor_integral = 40 * taxa
        valor_total = valor_integral + valor_taxa
        print(valor_total)
    elif hora < 40:
        valor1 = hora * taxa
        print(valor1)