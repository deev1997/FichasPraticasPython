horas = int(input("Introduza horas: "))
minutos = int(input("Introduza minutos: "))

if horas > 12:
    print(f"{horas-12}:{minutos}PM")

else:
    print(f"{horas}:{minutos}AM")