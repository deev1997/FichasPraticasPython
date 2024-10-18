def ler_inteiro():
    num = -1
    while num < 0:
        num = int(input("Introduza um número: "))
    return num

def imprimir(num):
    for i in range(num):
        print("*",end='')

n= ler_inteiro()

imprimir(n)