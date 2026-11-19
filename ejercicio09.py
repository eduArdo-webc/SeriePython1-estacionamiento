# Ejercicio 9. Control de capacidad
# (es el ejercicio 8 con un limite de 30 vehiculos)

capacidad = 30

total_vehiculos = 0
motos = 0
autos = 0
camionetas = 0
camiones = 0
total_dinero = 0

respuesta = "s"

while respuesta == "s" and total_vehiculos < capacidad:
    print("")
    placa = input("Ingrese la placa: ")
    print("1. Motocicleta  2. Automovil  3. Camioneta  4. Camion")
    tipo = int(input("Elija el tipo de vehiculo: "))
    horas = int(input("Ingrese las horas de estancia: "))

    if tipo == 1:
        tarifa = 10
        motos = motos + 1
    elif tipo == 2:
        tarifa = 15
        autos = autos + 1
    elif tipo == 3:
        tarifa = 20
        camionetas = camionetas + 1
    else:
        tarifa = 30
        camiones = camiones + 1

    importe = horas * tarifa
    print("El vehiculo", placa, "debe pagar: $", importe)

    total_vehiculos = total_vehiculos + 1
    total_dinero = total_dinero + importe

    disponibles = capacidad - total_vehiculos
    print("Espacios disponibles:", disponibles)

    if total_vehiculos == capacidad:
        print("El estacionamiento esta lleno, no es posible recibir mas vehiculos")
    else:
        respuesta = input("Desea registrar otro vehiculo? (s/n): ")

print("")
print("===== CORTE DE CAJA =====")
print("Total de vehiculos atendidos:", total_vehiculos)
print("Motocicletas:", motos)
print("Automoviles:", autos)
print("Camionetas:", camionetas)
print("Camiones:", camiones)
print("Importe total recaudado: $", total_dinero)
print("Espacios disponibles:", capacidad - total_vehiculos)
