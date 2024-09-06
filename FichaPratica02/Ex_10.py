print("Introduza um numero:")
num1 = int(input())
print("Introduza outro numero:")
num2 = int(input())
print("Qual a operacao aritmetica que quer fazer?")
op = input()

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