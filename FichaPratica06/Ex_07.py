myList = []

maiorPar = -1

for i in range(0, 10):
    myList.append(int(input("Digite um valor: ")))
    if myList[i] % 2 == 0 and maiorPar == -1:
        maiorPar = myList[i]

    if myList[i] % 2 == 0 and myList[i] > maiorPar:
        maiorPar = myList[i]

if maiorPar == -1:
    print("\nNão há pares")

else:
    print("\nO maior par é ", maiorPar)