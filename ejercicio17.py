# Ejercicio 17. Registro de vehiculos por cajon

estacionamiento = [
    ["ABC123", "LIBRE", "XYZ456"],
    ["LIBRE", "DEF789", "LIBRE"],
    ["GHI321", "LIBRE", "LIBRE"]
]

opcion = 0

while opcion != 4:
    print("")
    print("===== MENU =====")
    print("1. Ver estacionamiento")
    print("2. Registrar vehiculo")
    print("3. Buscar placa")
    print("4. Salir")
    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
        for i in range(3):
            print("Fila", i + 1, end=":  ")
            for j in range(3):
                print(estacionamiento[i][j], end="   ")
            print("")

    elif opcion == 2:
        placa = input("Ingrese la placa: ")
        fila = int(input("Ingrese la fila (1 a 3): "))
        espacio = int(input("Ingrese el espacio (1 a 3): "))

        if fila < 1 or fila > 3 or espacio < 1 or espacio > 3:
            print("Esa posicion no existe")
        elif estacionamiento[fila - 1][espacio - 1] == "LIBRE":
            estacionamiento[fila - 1][espacio - 1] = placa
            print("Vehiculo registrado en la fila", fila, "espacio", espacio)
        else:
            print("Ese espacio esta ocupado por", estacionamiento[fila - 1][espacio - 1])

    elif opcion == 3:
        buscar = input("Ingrese la placa a buscar: ")
        encontrado = False
        for i in range(3):
            for j in range(3):
                if estacionamiento[i][j] == buscar:
                    print("La placa", buscar, "esta en la fila", i + 1, "espacio", j + 1)
                    encontrado = True
        if encontrado == False:
            print("La placa no se encuentra en el estacionamiento")

    elif opcion == 4:
        print("Fin del programa")

    else:
        print("Opcion no valida")
