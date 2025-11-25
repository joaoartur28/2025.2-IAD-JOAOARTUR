# def serve para definir de maneira geral alguns nomes antes, sem precisar sair definindo nome por nome.
# Além disso, quando um termo é definido com def no inicio, as palavras utilizadas no inicio dentro do parênteses são automaticamente substituidas
# no final quando o mesmo termo utilizado é citado com outras palavras dentro do parênteses.

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
