tradutor = {
    "dog":"cachorro",
    "cat":"gato",
    "house":"casa",
    "car":"carro"
}

ingles = input("Digite o nome em ingles: ")

if ingles in tradutor:
    print(f"A tradução de {ingles} é {tradutor[ingles]}")