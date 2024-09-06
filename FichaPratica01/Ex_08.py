print("Introduza minutos da musica 1:")
min1 = int(input())
print("Introduza segundos da musica 1:")
seg1 = int(input())
print("Introduza minutos da musica 2:")
min2 = int(input())
print("Introduza segundos da musica 2:")
seg2 = int(input())
print("Introduza minutos da musica 3:")
min3 = int(input())
print("Introduza segundos da musica 3:")
seg3 = int(input())

min1 *= 60
min2 *= 60
min3 *= 60

total = min1 + min2 + min3 + seg1 + seg2 + seg3

horas = total // 3600
min = (total % 3600)//60
seg = total % 60

print(f"Total do album: {horas}h {min}m {seg}s")