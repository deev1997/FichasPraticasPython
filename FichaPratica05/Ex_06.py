# a) implementar uma função que determina se é par ou ímpar

def par(num):
    if num%2 == 0:
        return True
    else:
        return False

# b) implementar uma função que determina se um número é positivo ou negativo

def positivo(num):
    if num >= 0:
        return True
    else:
        return False

# c) implementar uma função que determina se um número é primo

def primo(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

# d) implementar uma função que determina se um número é perfeito

def perfeito(num):
    soma = 0
    for i in range(1,num):
        if num % i == 0:
            soma += i
    if soma == num:
        return True
    else:
        return False

# e) implementar uma função que determina se um número é triangular

def triangular(num):
    soma = 0
    for i in range(1,num):
        soma += i
        if soma == num:
            return True
    return False

"""if triangular(21):
    print("É triangular")
else:
    print("Não é triangular")"""