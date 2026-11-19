# Ejercicio 10. Historial de vehiculos

# lista vacia donde se van a guardar las placas
placas = []

respuesta = "s"

while respuesta == "s":
    placa = input("Ingrese la placa del vehiculo: ")
    placas.append(placa)
    print("Placa registrada")
    respuesta = input("Desea registrar otro vehiculo? (s/n): ")

# mostrar todas las placas
print("")
print("----- HISTORIAL DE VEHICULOS -----")
for i in range(len(placas)):
    print(i + 1, "-", placas[i])

print("Total de vehiculos registrados:", len(placas))
