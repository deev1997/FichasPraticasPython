salario = int(input("Introduza um salario:"))

if salario <= 15000:
    print(f"Paga taxa de 20%: {int(salario * 0.2)}€")
elif 15000 < salario <= 20000:
    print(f"Paga taxa de 30%: {int(salario * 0.3)}€")
elif 20000 < salario <= 25000:
    print(f"Paga taxa de 35%: {int(salario * 0.35)}€")
elif salario > 25000:
    print(f"Paga taxa de 40%: {int(salario * 0.4)}€")