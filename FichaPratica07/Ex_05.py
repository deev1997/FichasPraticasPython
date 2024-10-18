formandos = {
    "Joao": [8,7,9],
    "Maria": [16,19,18],
    "Ana": [19,18,20]
}

soma = 0

pesquisa = input("Introduza o nome do aluno para saber a média: ")

for i in range (0,len(formandos[pesquisa])):
    soma+=formandos[pesquisa][i]

media = soma/len(formandos[pesquisa])

print(media)