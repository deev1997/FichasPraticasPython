myList = [int(input("Digite um número: "))]

crescente = True
for i in range(1, 10):
    myList.append(int(input("Digite um número: ")))

    if myList[i-1] > myList[i]:
        crescente = False

if crescente:
    print("crescente")
else:
    print("não crescente")