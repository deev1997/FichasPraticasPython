num1 = int(input("Introduza um numero: "))
num2 = int(input("Introduza um numero: "))
num3 = int(input("Introduza um numero: "))

if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(f"Ordem crescente: {num1}, {num2}, {num3}")
    else:
        print(f"Ordem crescente: {num1}, {num3}, {num2}")
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(f"Ordem crescente: {num2}, {num1}, {num3}")
    else:
        print(f"Ordem crescente: {num2}, {num3}, {num1}")
else:  # num3 é o menor
    if num1 <= num2:
        print(f"Ordem crescente: {num3}, {num1}, {num2}")
    else:
        print(f"Ordem crescente: {num3}, {num2}, {num1}")