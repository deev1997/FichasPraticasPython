palavras = ["maçã","banana","laranja","maçã","laranja","laranja","pera","melão","melão"]

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)