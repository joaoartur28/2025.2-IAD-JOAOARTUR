def calcula_pagamento():
    print("--- Calculadora de Salário ---")

    e_funcionario = input("Você é um funcionário? (sim/não): ").strip().lower()

    if e_funcionario == "sim":
        print("Cálculo de salário para funcionários não aplicável.")
        return 

    try:
        horas_trabalhadas = float(input("Digite as Horas Trabalhadas: "))
        taxa_horaria = float(input("Digite a Taxa Horária de Pagamento: "))
    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos para horas e taxa.")
        return 

    pagamento_total = 0.0
    limite_horas_normais = 40

    if horas_trabalhadas > limite_horas_normais:
        horas_normais = limite_horas_normais
        pagamento_normal = horas_normais * taxa_horaria

        horas_extras = horas_trabalhadas - limite_horas_normais

        taxa_extra = taxa_horaria * 1.5
        pagamento_extra = horas_extras * taxa_extra

        pagamento_total = pagamento_normal + pagamento_extra

        print(f"\n--- Detalhes ---")
        print(f"Horas Normais: {horas_normais}h")
        print(f"Horas Extras: {horas_extras}h (com taxa de R$ {taxa_extra:.2f})")
        
    else:
        
        pagamento_total = horas_trabalhadas * taxa_horaria
        
        print(f"\n--- Detalhes ---")
        print(f"Todas as {horas_trabalhadas}h pagas pela taxa normal de R$ {taxa_horaria:.2f}.")

    print(f"\nPagamento Total: R$ {pagamento_total:.2f}")

calcula_pagamento()