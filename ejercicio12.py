# Ejercicio 12. Control de ingresos y egresos

capacidad = 15
placas = []

opcion = 0

while opcion != 6:
    print("")
    print("===== ESTACIONAMIENTO =====")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Ver vehiculos dentro")
    print("4. Ver cuantos vehiculos hay")
    print("5. Ver espacios disponibles")
    print("6. Salir")
    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
        # revisar si esta lleno
        if len(placas) == capacidad:
            print("El estacionamiento esta lleno, no se puede recibir mas vehiculos")
        else:
            placa = input("Ingrese la placa: ")
            placas.append(placa)
            print("Vehiculo registrado")

    elif opcion == 2:
        placa = input("Ingrese la placa del vehiculo que sale: ")
        # buscar la placa en la lista
        encontrado = False
        for i in range(len(placas)):
            if placas[i] == placa:
                encontrado = True

        if encontrado == True:
            placas.remove(placa)
            print("Salida registrada")
        else:
            print("Esa placa no esta registrada, no se puede dar salida")

    elif opcion == 3:
        if len(placas) == 0:
            print("No hay vehiculos dentro")
        else:
            print("Vehiculos dentro del estacionamiento:")
            for i in range(len(placas)):
                print(i + 1, "-", placas[i])

    elif opcion == 4:
        print("Vehiculos estacionados:", len(placas))

    elif opcion == 5:
        disponibles = capacidad - len(placas)
        print("Espacios disponibles:", disponibles)

    elif opcion == 6:
        print("Fin del programa")

    else:
        print("Opcion no valida")
