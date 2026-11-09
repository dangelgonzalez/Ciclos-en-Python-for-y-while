suma = 0
cantidad = 0
nota = float(input("Nota (-1 para terminar): "))

while nota != -1:
    suma += nota
    cantidad += 1
    nota = float(input("Nota (-1 para terminar): "))

if cantidad > 0:
    promedio = suma / cantidad
    print("Promedio:", promedio)
else:
    print("No ingresaste notas")