mes1 = int(input("Introduza o salario de Janeiro: "))
mes2 = int(input("Introduza o salario de Fevereiro: "))
mes3 = int(input("Introduza o salario de Março: "))
mes4 = int(input("Introduza o salario de Abril: "))
mes5 = int(input("Introduza o salario de Maio: "))
mes6 = int(input("Introduza o salario de Junho: "))
mes7 = int(input("Introduza o salario de Julho: "))
mes8 = int(input("Introduza o salario de Agosto: "))
mes9 = int(input("Introduza o salario de Setembro: "))
mes10 = int(input("Introduza o salario de Outubro: "))
mes11 = int(input("Introduza o salario de Novembro: "))
mes12 = int(input("Introduza o salario de Dezembro: "))

sal_medio = (mes1+mes2+mes3+mes4+mes5+mes6+mes7+mes8+mes9+mes10+mes11+mes12) / 12

print(f"Salário médio: {sal_medio:.2f}€")

if 0 <= sal_medio <= 2000:
    print("Nenhum crédito")

elif 2000 < sal_medio <= 4000:
    print(f"Crédito vai ser de {sal_medio*0.2:.2f}€")

elif 4000 < sal_medio <= 6000:
    print(f"Crédito vai ser de {sal_medio*0.3:.2f}€")

elif sal_medio > 6000:
    print(f"Crédito vai ser de {sal_medio*0.4:.2f}€")