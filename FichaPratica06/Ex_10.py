myList = []
posicao = []
existe = False

for i in range(0, 10):
    myList.append(int(input('Digite um valor: ')))

num = int(input('Número a pesquisar: '))

for i in range(0, 10):
    if myList[i] == num:
        existe = True
        posicao.append(i)

if existe:
    for i in range(0, len(posicao)):
        print(f"Array[{posicao[i]}]")
else:
    print(f"{num} não existe no Array ")