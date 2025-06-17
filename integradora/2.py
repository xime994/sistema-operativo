cargas = []
while True:
    carga = float(input("Litros cargados (0 para terminar): "))
    if carga == 0:
        break
    cargas.append(carga)
    if carga < 5:
        print("Carga menor a 5 litros. Posible error.")

total = sum(cargas)
promedio = total / len(cargas) if cargas else 0

print(f"Total cargado: {total} litros")
print(f"Promedio por carga: {promedio:.2f} litros")