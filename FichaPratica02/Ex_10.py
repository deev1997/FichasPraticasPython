num1 = int(input("Introduza um numero:"))
num2 = int(input("Introduza outro numero:"))
op = input("Qual a operacao aritmetica que quer fazer?")

if op == '+':
    print(f"{num1} + {num2} = {num1+num2}")
elif op == '-':
    print(f"{num1} - {num2} = {num1-num2}")
elif op == '*':
    print(f"{num1} * {num2} = {num1*num2}")
elif op == '/':
    print(f"{num1} / {num2} = {num1/num2}")
else:
    print("Erro")