lim = int(input("Quantos números deseja inserir: "))

crescente = True

anterior = int(input("Introduza um número: "))

for i in range(1, lim):
    atual = int(input("Introduza um número: "))
    if atual < anterior:
        crescente = False
    anterior = atual

if crescente:
    print("Crescente")
else:
    print("Não crescente")