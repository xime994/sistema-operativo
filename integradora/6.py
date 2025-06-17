donaciones = []

while True:
    donacion = float(input("Ingresá una donación (0 para terminar): "))
    if donacion == 0:
        break
    donaciones.append(donacion)

if donaciones:
    total = sum(donaciones)
    mayor = max(donaciones)
    cantidad = len(donaciones)
    print(f"Total recaudado: ${total}")
    print(f"Mayor donación: ${mayor}")
    print(f"Cantidad de personas que donaron: {cantidad}")
else:
    print("No hubo donaciones.")