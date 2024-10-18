"""from FichaPratica06.Ex_01 import create_list

myList = create_list(10)

myList.sort()

print(myList[0])"""

myList = [int(input('Digite um valor: '))]
menor = myList[0]
for i in range(1,10):
    myList.append(int(input('Digite um valor: ')))
    if myList[i] < menor:
        menor = myList[i]
print(menor)