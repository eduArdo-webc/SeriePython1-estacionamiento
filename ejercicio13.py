# Ejercicio 13. Distribucion de espacios
# 0 = espacio libre
# 1 = espacio ocupado

estacionamiento = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0]
]

print("DISTRIBUCION DEL ESTACIONAMIENTO")
print("(0 = libre, 1 = ocupado)")
print("")
print("        E1 E2 E3 E4 E5")

# ciclos anidados para recorrer filas y columnas
for i in range(4):
    print("Fila", i + 1, end="  ")
    for j in range(5):
        print(estacionamiento[i][j], end="  ")
    print("")
