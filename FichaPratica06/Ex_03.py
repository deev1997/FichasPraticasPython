from FichaPratica06.Ex_01 import create_list

myList = []

"""myList = create_list(10)

myList.sort()
print(myList[9])"""

myList.append(int(input('Digite um valor: ')))
maior = myList[0]
for i in range(1,10):
    myList.append(int(input('Digite um valor: ')))
    if myList[i] > maior:
        maior = myList[i]
print(maior)