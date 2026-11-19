# Ejercicio 7. Atencion de varios vehiculos

respuesta = "s"

while respuesta == "s":
    print("")
    placa = input("Ingrese la placa: ")
    print("1. Motocicleta  2. Automovil  3. Camioneta  4. Camion")
    tipo = int(input("Elija el tipo de vehiculo: "))
    horas = int(input("Ingrese las horas de estancia: "))

    if tipo == 1:
        tarifa = 10
    elif tipo == 2:
        tarifa = 15
    elif tipo == 3:
        tarifa = 20
    else:
        tarifa = 30

    importe = horas * tarifa

    print("El vehiculo", placa, "debe pagar: $", importe)

    respuesta = input("Desea registrar otro vehiculo? (s/n): ")

print("Fin del registro")
