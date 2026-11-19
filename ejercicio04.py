# Ejercicio 4. Tarifas diferenciadas

horas = int(input("Ingrese las horas de estancia: "))

if horas <= 2:
    tarifa = 20
elif horas <= 5:
    tarifa = 18
else:
    tarifa = 15

importe = horas * tarifa

print("")
print("Tarifa por hora: $", tarifa)
print("Importe a pagar: $", importe)
