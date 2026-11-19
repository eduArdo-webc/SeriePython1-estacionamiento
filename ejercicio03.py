# Ejercicio 3. Cobro por tiempo de permanencia

tarifa = 15

tiempo = float(input("Ingrese el tiempo de permanencia en horas (ejemplo 2.5): "))

# se toma solo la parte entera de las horas
horas_cobrar = int(tiempo)

# si sobra un pedazo de hora, se cobra la hora completa
if tiempo > horas_cobrar:
    horas_cobrar = horas_cobrar + 1

importe = horas_cobrar * tarifa

print("")
print("Horas a cobrar:", horas_cobrar)
print("Importe a pagar: $", importe)
