minutos = []

for i in range(7):
    ejercicio = int(input(f"Minutos de ejercicio del día {i+1}: "))
    minutos.append(ejercicio)

promedio = sum(minutos) / 7
print(f"Promedio diario de ejercicio: {promedio:.2f} minutos")

if promedio < 30:
    print("Deberías hacer más ejercicio.")
else:
    print("¡Bien hecho con tu actividad física!")