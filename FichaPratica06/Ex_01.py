def create_list (num):
    lista = []
    for i in range(num):
        numero = int(input("Insira: "))
        lista.append(numero)
    return lista

if __name__ == "__main__":
    myLista = create_list(10)
    print(myLista)