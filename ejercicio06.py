# Ejercicio 6. Clasificacion del tipo de vehiculo

print("Tipos de vehiculo:")
print("1. Motocicleta ($10 por hora)")
print("2. Automovil ($15 por hora)")
print("3. Camioneta ($20 por hora)")
print("4. Camion ($30 por hora)")

tipo = int(input("Elija el tipo de vehiculo: "))
horas = int(input("Ingrese las horas de estancia: "))

if tipo == 1:
    nombre = "Motocicleta"
    tarifa = 10
elif tipo == 2:
    nombre = "Automovil"
    tarifa = 15
elif tipo == 3:
    nombre = "Camioneta"
    tarifa = 20
elif tipo == 4:
    nombre = "Camion"
    tarifa = 30
else:
    nombre = "No valido"
    tarifa = 0

if tarifa == 0:
    print("Tipo de vehiculo no valido")
else:
    importe = horas * tarifa
    print("")
    print("Vehiculo:", nombre)
    print("Tarifa por hora: $", tarifa)
    print("Importe a pagar: $", importe)
