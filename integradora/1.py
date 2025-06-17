LIMITE = 100000  # podés cambiar este valor

total = 0
while True:
    gasto = float(input("Ingresá un gasto (0 para terminar): "))
    if gasto == 0:
        break
    total += gasto

print(f"Total gastado: ${total}")
if total > LIMITE:
    print("Se superó el límite presupuestado.")
else:
    print("Todo dentro del presupuesto.")