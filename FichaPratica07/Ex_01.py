animais = {

    "a":["andorinha", "avestruz", "alforreca"],
    "b":["baleia", "bisonte"],
    "c":["carnacia","camelo"],
    "d":["dromedario", "doninha"]

}

op = input("Introduza uma letra para imprimir dicionario:")

for animal in animais[op]:
    print(animal)