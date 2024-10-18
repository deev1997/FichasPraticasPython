num = int(input("Introduza um número: "))

bool = True

for i in range(2, num):
    if num % i == 0:
        bool = False

if bool:
    print("É primo")
else:
    print("Não é primo")