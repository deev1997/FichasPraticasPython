myList = []

for i in range(0, 10):
    myList.append(int(input('Digite um valor: ')))

myList.sort(reverse=True)

print(myList)