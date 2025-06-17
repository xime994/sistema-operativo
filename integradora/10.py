combustible = 0  # en litros
CONSUMO_POR_KM = 0.07

while True:
    accion = input("¿Querés 'cargar', 'consumir' o 'salir'? ").lower()

    if accion == 'cargar':
        litros = float(input("Litros a cargar: "))
        combustible += litros
    elif accion == 'consumir':
        litros = float(input("Litros consumidos: "))
        combustible -= litros
        if combustible < 0:
            combustible = 0
    elif accion == 'salir':
        break
    else:
        print("Opción no válida.")

if combustible < 50 * CONSUMO_POR_KM:
    print("No hay suficiente combustible para recorrer 50 km.")
else:
    print("Combustible suficiente para 50 km.")