from FichaPratica05.Ex_06 import par, positivo, primo, perfeito, triangular

numero = int(input("Numero: "))

op = 10
while op != 7:
    print(f"***** ANÁLISE DO NUMERO {numero} *****")
    print("1. Par ou Ímpar")
    print("2. Positivo ou Negativo")
    print("3. Primo ou Não Primo")
    print("4. Perfeito ou Não Perfeito")
    print("5. Triangular ou Não Triangular")
    print("6. Trocar de Número")
    print("7. Sair")

    op = int(input("Opção: "))

    match op:
        case 1:
            if par(numero):
                print("É par\n")
            else:
                print("É ímpar\n")
        case 2:
            if positivo(numero):
                print("É positivo\n")
            else:
                print("É negativo\n")
        case 3:
            if primo(numero):
                print("É primo\n")
            else:
                print("É não primo\n")
        case 4:
            if perfeito(numero):
                print("É perfeito\n")
            else:
                print("É não perfeito\n")
        case 5:
            if triangular(numero):
                print("É triangular\n")
            else:
                print("É não triangular\n")
        case 6:
            numero = int(input("Digite outro número: "))
        case 7:
            break