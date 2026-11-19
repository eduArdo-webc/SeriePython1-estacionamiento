# Ejercicio 18. Registro de cobros por vehiculo

# matriz del estacionamiento (3 filas, 3 espacios)
estacionamiento = [
    ["ABC123", "XYZ456", "DEF789"],
    ["LIBRE", "LIBRE", "LIBRE"],
    ["LIBRE", "LIBRE", "LIBRE"]
]

# listas con la informacion de cada vehiculo
# (la misma posicion en todas las listas es el mismo vehiculo)
placas = ["ABC123", "XYZ456", "DEF789"]
tipos = ["Auto", "Moto", "Auto"]
entradas = [8, 9, 10]
salidas = ["-", "-", "-"]
permanencias = ["-", "-", "-"]
importes = ["-", "-", "-"]

opcion = 0

while opcion != 5:
    print("")
    print("===== MENU =====")
    print("1. Ver estacionamiento")
    print("2. Registrar entrada")
    print("3. Registrar salida y cobrar")
    print("4. Ver tabla de registros")
    print("5. Salir")
    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
        for i in range(3):
            print("Fila", i + 1, end=":  ")
            for j in range(3):
                print(estacionamiento[i][j], end="   ")
            print("")

    elif opcion == 2:
        placa = input("Ingrese la placa: ")
        print("Tipo de vehiculo: 1.Moto  2.Auto  3.Camioneta  4.Camion")
        t = int(input("Elija el tipo: "))
        if t == 1:
            tipo = "Moto"
        elif t == 2:
            tipo = "Auto"
        elif t == 3:
            tipo = "Camioneta"
        else:
            tipo = "Camion"
        hora = int(input("Hora de entrada (0 a 23): "))
        fila = int(input("Fila (1 a 3): "))
        espacio = int(input("Espacio (1 a 3): "))

        if fila < 1 or fila > 3 or espacio < 1 or espacio > 3:
            print("Esa posicion no existe")
        elif estacionamiento[fila - 1][espacio - 1] != "LIBRE":
            print("Ese espacio esta ocupado, elija otro")
        else:
            estacionamiento[fila - 1][espacio - 1] = placa
            placas.append(placa)
            tipos.append(tipo)
            entradas.append(hora)
            salidas.append("-")
            permanencias.append("-")
            importes.append("-")
            print("Vehiculo registrado")

    elif opcion == 3:
        buscar = input("Ingrese la placa del vehiculo que sale: ")

        # buscar la placa en la matriz
        fila = -1
        espacio = -1
        for i in range(3):
            for j in range(3):
                if estacionamiento[i][j] == buscar:
                    fila = i
                    espacio = j

        if fila == -1:
            print("Esa placa no esta en el estacionamiento")
        else:
            print("El vehiculo esta en la fila", fila + 1, "espacio", espacio + 1)

            # buscar el vehiculo en las listas (el que todavia no ha salido)
            pos = -1
            for k in range(len(placas)):
                if placas[k] == buscar and salidas[k] == "-":
                    pos = k

            hora_salida = int(input("Hora de salida (0 a 23): "))

            if hora_salida < entradas[pos]:
                print("La hora de salida no puede ser antes de la entrada")
            else:
                tiempo = hora_salida - entradas[pos]
                # si estuvo menos de una hora se cobra la hora completa
                if tiempo < 1:
                    tiempo = 1

                # tarifa segun el tipo
                if tipos[pos] == "Moto":
                    tarifa = 10
                elif tipos[pos] == "Auto":
                    tarifa = 15
                elif tipos[pos] == "Camioneta":
                    tarifa = 20
                else:
                    tarifa = 30

                importe = tiempo * tarifa

                salidas[pos] = hora_salida
                permanencias[pos] = tiempo
                importes[pos] = importe

                # liberar el espacio
                estacionamiento[fila][espacio] = "LIBRE"

                print("----- TICKET -----")
                print("Placa:", placas[pos])
                print("Tipo:", tipos[pos])
                print("Hora entrada:", entradas[pos])
                print("Hora salida:", hora_salida)
                print("Permanencia:", tiempo, "horas")
                print("Importe a pagar: $", importe)
                print("Espacio liberado")

    elif opcion == 4:
        print("No.\tPlaca\tTipo\tEntrada\tSalida\tHoras\tImporte")
        for k in range(len(placas)):
            print(k + 1, "\t", placas[k], "\t", tipos[k], "\t", entradas[k], "\t", salidas[k], "\t", permanencias[k], "\t", importes[k])

    elif opcion == 5:
        print("Fin del programa")

    else:
        print("Opcion no valida")
