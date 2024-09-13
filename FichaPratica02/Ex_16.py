euros = int(input("Introduza um valor em euros múltiplo de 5: "))

notas200 = 0
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0

if euros >= 200:
    notas200 = euros // 200
    euros = euros % 200
if euros >= 100:
    notas100 = euros // 100
    euros = euros % 100
if euros >= 50:
    notas50 = euros // 50
    euros = euros % 50
if euros >= 20:
    notas20 = euros // 20
    euros = euros % 20
if euros >= 10:
    notas10 = euros // 10
    euros = euros % 10
if euros >= 5:
    notas5 = euros // 5
    euros = euros % 5

print(f"Notas de 200: {notas200}")
print(f"Notas de 100: {notas100}")
print(f"Notas de 50: {notas50}")
print(f"Notas de 20: {notas20}")
print(f"Notas de 10: {notas10}")
print(f"Notas de 5: {notas5}")