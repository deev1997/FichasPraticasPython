saldo = int(input("Introduza o saldo da conta bancaria:"))
movimento = int(input("Introduza o montante a creditar/debitar:"))

if (saldo+movimento) > 0:
    print("Operação Válida")
else:
    print("Operação Inválida")