num = int(input("Ingrese el valor de num: "))
V = int(input("Ingrese el valor de V: "))
if num == 1:
    val = 100 * V
elif num == 2:
    val = 100 ** V
elif num == 3:
    if V != 0:
        val = 100 / V
    else:
        val = "Error: no se puede dividir por cero"
else:
    val = 0

print("El valor de val es:", val)