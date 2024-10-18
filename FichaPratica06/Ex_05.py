myList = []
i = 0
soma = 0

while True:
    myList.append(int(input("Digite um valor: ")))
    if myList[i] < 0:
        break
    else:
        soma += myList[i]
        i += 1

media = soma / i

print(media)