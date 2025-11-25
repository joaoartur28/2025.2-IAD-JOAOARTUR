def calculoPagamento(horas, taxaHora):
    if horas > 40:
        valor_taxa = horas - 40
        pagamento = (40 * taxaHora) + (valor_taxa * taxaHora * 1.5)
    else:
        pagamento = horas * taxaHora
    return pagamento


horas = float(input("Insira as Horas: "))
taxa = float(input("Insira o valor da Hora de Trabalho: "))

resultado = calculoPagamento(horas, taxa)
print("pagamento:", resultado)
