num = None
soma = 0
i = 0

while num != -1:
    num = int(input("Introduza um número: "))
    if num != -1:
        soma += num
        i += 1

print(f"Média: {soma / i:.2f}")