num1 = int(input("Introduza um numero:"))
num2 = int(input("Introduza um numero:"))
num3 = int(input("Introduza um numero:"))

menor = num1
if num2 < menor:
    menor = num2
    print(f"Menor numero é {menor}")
elif num3 < menor:
    menor = num3
    print(f"Menor numero é {menor}")
else:
    print(f"Menor numero é {num1}")