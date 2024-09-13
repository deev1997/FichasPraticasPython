num = 0

primeiro = 0
segundo = 0
terceiro = 0
quarto = 0

while num >= 0:
    num = int(input("Introduza um número: "))
    if 0 <= num <= 25:
        primeiro = primeiro + 1
    elif 25 < num <= 50:
        segundo = segundo + 1
    elif 50 < num <= 75:
        terceiro = terceiro + 1
    elif 75 < num <= 100:
        quarto = quarto + 1

print(f"[00,25]: {primeiro}")
print(f"[26,50]: {segundo}")
print(f"[51,75]: {terceiro}")
print(f"[76,100]: {quarto}")