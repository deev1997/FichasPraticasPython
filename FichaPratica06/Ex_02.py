comissoes = []
total = 0
for i in range(12):
    comissoes.append(int(input("Introduza a comissão mensal: ")))
    total += comissoes[i]
print(total)