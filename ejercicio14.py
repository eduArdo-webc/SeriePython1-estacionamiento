# Ejercicio 14. Registro de ocupacion

estacionamiento = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0]
]

respuesta = "s"

while respuesta == "s":
    # mostrar como esta el estacionamiento
    print("")
    print("        E1 E2 E3 E4 E5")
    for i in range(4):
        print("Fila", i + 1, end="  ")
        for j in range(5):
            print(estacionamiento[i][j], end="  ")
        print("")

    print("")
    fila = int(input("Ingrese el numero de fila (1 a 4): "))
    espacio = int(input("Ingrese el numero de espacio (1 a 5): "))

    # revisar que la posicion exista
    if fila < 1 or fila > 4 or espacio < 1 or espacio > 5:
        print("Esa posicion no existe")
    else:
        # se resta 1 porque en python las posiciones empiezan en 0
        if estacionamiento[fila - 1][espacio - 1] == 0:
            estacionamiento[fila - 1][espacio - 1] = 1
            print("Vehiculo estacionado en la fila", fila, "espacio", espacio)
        else:
            print("Ese espacio ya esta ocupado, seleccione otro lugar")

    respuesta = input("Desea registrar otro vehiculo? (s/n): ")
