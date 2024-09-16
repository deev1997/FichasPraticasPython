salario = int(input("Introduza um salario:"))

if salario <= 15000:
    print(f"Paga taxa de 20%: {int(salario*0.2)}€")

else:
    print(f"Paga taxa de 30%: {int(salario*0.3)}€")
