inicio = int(input("Introduza um número: "))
fim = int(input("Introduza um número: "))

for i in range(inicio, fim + 1):
    if i % 5 == 0:
        print(i)