print("\nMenu:")
print("1. Criar")
print("2. Atualizar")
print("3. Eliminar")
print("4. Sair")

op = input("Escolha uma opção (1, 2, 3 ou 4): ")

match op:
    case "1":
        print("Criar")
    case "2":
        print("Atualizar")
    case "3":
        print("Eliminar")
    case "4":
        # Não faz nada se a opção for 4
        pass
    case _:
        print("Opção inválida!")