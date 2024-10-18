listaContactos = []

print("1 - Inserir um novo contacto")
print("2 - Imprime todos os contactos")
print("3 - Pesquisar um contacto")
print("4 - Sair do programa")

print("")

op = 0
while op != 4:
    op = int(input("Insira a opção que deseja: "))

    match op:
        case 1:
            contactos = {
                "nome": input("Insira o nome do contacto: "),
                "telefone": input("Insira o telefone do contacto: "),
                "morada": input("Insira a morada do contacto: ")
            }
            listaContactos.append(contactos)
        case 2:
            for i in range(0, len(listaContactos)):
                print("Nome: ", listaContactos[i]["nome"])
                print("Telefone: ", listaContactos[i]["telefone"])
                print("Morada: ", listaContactos[i]["morada"])
                print("______________________________________________")
        case 3:
            pesquisa = input("Insira o nome do contacto: ")
            for i in range(0, len(listaContactos)):
                if pesquisa == listaContactos[i]["nome"]:
                    print(f'O seu telefone é {listaContactos[i]['telefone']} e a sua morada é {listaContactos[i]['morada']}.')
        case 4:
            break