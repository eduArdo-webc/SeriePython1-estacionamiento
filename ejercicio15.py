# Ejercicio 15. Conteo de espacios disponibles

estacionamiento = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0]
]

total = 0
ocupados = 0
libres = 0

# recorrer toda la matriz y contar
for i in range(4):
    for j in range(5):
        total = total + 1
        if estacionamiento[i][j] == 1:
            ocupados = ocupados + 1
        else:
            libres = libres + 1

porcentaje = ocupados * 100 / total

print("----- OCUPACION DEL ESTACIONAMIENTO -----")
print("Total de espacios:", total)
print("Espacios ocupados:", ocupados)
print("Espacios libres:", libres)
print("Porcentaje de ocupacion:", porcentaje, "%")
