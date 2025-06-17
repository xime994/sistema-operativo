LIMITE = 20000
total = 0

while total < LIMITE:
    compra = float(input("Ingresá el monto de la compra: "))
    if total + compra > LIMITE:
        print("No se puede realizar esta compra, excede el límite.")
        break
    total += compra

print(f"Total gastado en el día: ${total}")