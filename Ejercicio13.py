palabra = input("Escribe una palabra:")
vocales = 0

for letra in palabra:
    if letra in "auiou":
        vocales += 1

print("Tiene", vocales, "vocales")