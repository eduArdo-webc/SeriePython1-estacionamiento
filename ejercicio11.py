# Ejercicio 11. Busqueda de vehiculos

placas = []

# primero se registran las placas
respuesta = "s"
while respuesta == "s":
    placa = input("Ingrese la placa del vehiculo: ")
    placas.append(placa)
    respuesta = input("Desea registrar otra placa? (s/n): ")

print("")

# ahora se busca una placa
buscar = input("Ingrese la placa que desea buscar: ")

encontrado = False
posicion = 0

# se recorre la lista y se compara cada placa
for i in range(len(placas)):
    if placas[i] == buscar:
        encontrado = True
        posicion = i

if encontrado == True:
    print("La placa", buscar, "SI esta en el historial")
    print("Se encuentra en la posicion", posicion + 1, "de la lista")
else:
    print("La placa", buscar, "NO esta en el historial")
