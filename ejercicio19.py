# Ejercicio 19. Reporte de ocupacion e ingresos
# (es el ejercicio 18 con una opcion mas para el reporte)

estacionamiento = [
    ["ABC123", "XYZ456", "DEF789"],
    ["LIBRE", "LIBRE", "LIBRE"],
    ["LIBRE", "LIBRE", "LIBRE"]
]

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
    print("1. Registrar entrada")
    print("2. Registrar salida y cobrar")
    print("3. Ver tabla de registros")
    print("4. Reporte del dia")
    print("5. Salir")
    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
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

    elif opcion == 2:
        buscar = input("Ingrese la placa del vehiculo que sale: ")

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
            pos = -1
            for k in range(len(placas)):
                if placas[k] == buscar and salidas[k] == "-":
                    pos = k

            hora_salida = int(input("Hora de salida (0 a 23): "))

            if hora_salida < entradas[pos]:
                print("La hora de salida no puede ser antes de la entrada")
            else:
                tiempo = hora_salida - entradas[pos]
                if tiempo < 1:
                    tiempo = 1

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
                estacionamiento[fila][espacio] = "LIBRE"

                print("Permanencia:", tiempo, "horas")
                print("Importe a pagar: $", importe)
                print("Espacio liberado")

    elif opcion == 3:
        print("No.\tPlaca\tTipo\tEntrada\tSalida\tHoras\tImporte")
        for k in range(len(placas)):
            print(k + 1, "\t", placas[k], "\t", tipos[k], "\t", entradas[k], "\t", salidas[k], "\t", permanencias[k], "\t", importes[k])

    elif opcion == 4:
        print("")
        print("========== REPORTE DEL DIA ==========")

        # 1. vehiculos que siguen dentro
        print("1. Vehiculos dentro del estacionamiento:")
        hay = False
        for i in range(3):
            for j in range(3):
                if estacionamiento[i][j] != "LIBRE":
                    print("   ", estacionamiento[i][j], "- fila", i + 1, "espacio", j + 1)
                    hay = True
        if hay == False:
            print("   No hay vehiculos dentro")

        # 2. espacios libres y ocupados
        libres = 0
        ocupados = 0
        for i in range(3):
            for j in range(3):
                if estacionamiento[i][j] == "LIBRE":
                    libres = libres + 1
                else:
                    ocupados = ocupados + 1
        print("2. Espacios ocupados:", ocupados, " Espacios libres:", libres)

        # 3. total de vehiculos atendidos
        print("3. Total de vehiculos atendidos:", len(placas))

        # 4. ingresos (solo de los que ya pagaron)
        total = 0
        for k in range(len(importes)):
            if importes[k] != "-":
                total = total + importes[k]
        print("4. Ingresos generados: $", total)

        # 5. tipo de vehiculo que mas entro
        motos = 0
        autos = 0
        camionetas = 0
        camiones = 0
        for k in range(len(tipos)):
            if tipos[k] == "Moto":
                motos = motos + 1
            elif tipos[k] == "Auto":
                autos = autos + 1
            elif tipos[k] == "Camioneta":
                camionetas = camionetas + 1
            else:
                camiones = camiones + 1

        mayor_tipo = "Moto"
        mayor_cantidad = motos
        if autos > mayor_cantidad:
            mayor_tipo = "Auto"
            mayor_cantidad = autos
        if camionetas > mayor_cantidad:
            mayor_tipo = "Camioneta"
            mayor_cantidad = camionetas
        if camiones > mayor_cantidad:
            mayor_tipo = "Camion"
            mayor_cantidad = camiones
        print("5. Tipo con mas ingresos:", mayor_tipo, "con", mayor_cantidad, "vehiculos")

        # 6. fila con mayor ocupacion
        mayor = -1
        fila_mayor = 0
        for i in range(3):
            cuenta = 0
            for j in range(3):
                if estacionamiento[i][j] != "LIBRE":
                    cuenta = cuenta + 1
            if cuenta > mayor:
                mayor = cuenta
                fila_mayor = i + 1
        print("6. Fila con mayor ocupacion: fila", fila_mayor, "con", mayor, "vehiculos")

    elif opcion == 5:
        print("Fin del programa")

    else:
        print("Opcion no valida")
