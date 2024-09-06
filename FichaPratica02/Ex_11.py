print("Introduza o saldo da conta bancaria:")
saldo = int(input())
print("Introduza o montante a creditar/debitar:")
movimento = int(input())

if (saldo+movimento) > 0:
    print("Operação Válida")
else:
    print("Operação Inválida")