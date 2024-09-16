nota1 = float(input("Introduza nota 1:"))
nota2 = float(input("Introduza nota 2:"))
nota3 = float(input("Introduza nota 3:"))

media_pond = (nota1*0.25)+(nota2*0.35)+(nota3*0.4)

if media_pond > 9.5:
    print("Aprovado")
else:
    print("Reprovado")