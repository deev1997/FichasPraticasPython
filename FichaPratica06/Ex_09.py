myList = []
existe = False

for i in range(0, 10):
    myList.append(int(input('Digite um valor: ')))

num = int(input('Número a pesquisar: '))

for i in range(0, 10):
    if myList[i] == num:
        existe = True
        break

if existe:
    print(f"{num} existe na lista!")
else:
    print(f"{num} não existe na lista!")