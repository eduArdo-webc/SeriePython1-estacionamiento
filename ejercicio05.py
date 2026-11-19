# Ejercicio 5. Descuentos para clientes frecuentes

visitas = int(input("Ingrese el numero de visitas del cliente este mes: "))
importe = float(input("Ingrese el importe de la estancia: $"))

if visitas > 10:
    descuento = importe * 0.10
    print("Cliente frecuente, tiene 10% de descuento")
else:
    descuento = 0
    print("Cliente sin descuento")

total = importe - descuento

print("")
print("Importe:", importe)
print("Descuento:", descuento)
print("Total a pagar: $", total)
