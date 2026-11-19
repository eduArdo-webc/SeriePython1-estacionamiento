# Ejercicio 16. Fila con mayor ocupacion

estacionamiento = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0]
]

mayor = -1
fila_mayor = 0

for i in range(4):
    ocupados = 0
    libres = 0
    # contar los espacios de esta fila
    for j in range(5):
        if estacionamiento[i][j] == 1:
            ocupados = ocupados + 1
        else:
            libres = libres + 1

    print("Fila", i + 1, "-> ocupados:", ocupados, " libres:", libres)

    # ver si esta fila tiene mas que la mayor hasta ahora
    if ocupados > mayor:
        mayor = ocupados
        fila_mayor = i + 1

print("")
print("La fila con mayor ocupacion es la fila", fila_mayor, "con", mayor, "vehiculos")
