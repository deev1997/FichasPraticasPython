num1 = int(input("Introduza um numero: "))
num2 = int(input("Introduza um numero: "))
num3 = int(input("Introduza um numero: "))
op = input("Introduza C ou D: ")

if op == "C":
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
    else:
        if num1 <= num2:
            print(f"Ordem crescente: {num3}, {num1}, {num2}")
        else:
            print(f"Ordem crescente: {num3}, {num2}, {num1}")

elif op == "D":
    if num1 <= num2 and num1 <= num3:
        if num2 <= num3:
            print(f"Ordem decrescente: {num3}, {num2}, {num1}")
        else:
            print(f"Ordem decrescente: {num2}, {num3}, {num1}")
    elif num2 <= num1 and num2 <= num3:
        if num1 <= num3:
            print(f"Ordem decrescente: {num3}, {num1}, {num2}")
        else:
            print(f"Ordem decrescente: {num1}, {num3}, {num2}")
    else:
        if num1 <= num2:
            print(f"Ordem decrescente: {num2}, {num1}, {num3}")
        else:
            print(f"Ordem decrescente: {num1}, {num2}, {num3}")