stock_original = int(input("Ingresá el stock inicial: "))
stock = stock_original

while stock > 0:
    vendidos = int(input("Cantidad vendida (0 para salir): "))
    if vendidos == 0:
        break
    if vendidos <= stock:
        stock -= vendidos
    else:
        print("No hay suficiente stock.")

    if stock <= stock_original * 0.1:
        print("Stock bajo (menos del 10%).")

print("Stock agotado o programa finalizado.")