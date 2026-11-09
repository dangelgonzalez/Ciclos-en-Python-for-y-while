secreto = 7
intento = int(input("Adivina el número secreto (entre 1 y 10): "))

while intento != secreto:
    if intento < secreto:
        print("Muy alto")
    else:
        print("Muy bajo")
    intento = int(input("Intenta de nuevo: "))  

print("¡Acertaste!") 
