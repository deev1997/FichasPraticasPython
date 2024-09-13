n = int(input("Introduza um número: "))

i = n-1
fatorial = n

while i > 0:
    fatorial = fatorial*i
    i = i-1

print(fatorial)

"""
n = int(input("Introduza um número: "))
resultado = 1

if n == 0 or n == 1:
    resultado = 1
else:
    for i in range(2, n + 1):
        temp = 0
        contador = 0
        while contador < i:
            temp += resultado
            contador += 1
        resultado = temp

print(f"Fatorial de {n} é {resultado}")
"""