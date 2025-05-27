
temperaturas = []

for i in range(7):
    temp = float(input(f"Ingrese la temperatura máxima del día {i+1}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / len(temperaturas)

dias_calurosos = 0
for temp in temperaturas:
    if temp > 30:
        dias_calurosos += 1

print(f"\nTemperaturas registradas: {temperaturas}")
print(f"Temperatura media de la semana: {media:.2f}°C")
print(f"Número de días con temperatura mayor a 30°C: {dias_calurosos}")