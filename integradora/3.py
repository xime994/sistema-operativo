agua = []
for dia in range(1, 8):
    vasos = int(input(f"Vasos de agua tomados el día {dia}: "))
    agua.append(vasos)

promedio = sum(agua) / 7
print(f"Promedio diario: {promedio:.2f} vasos")
if promedio < 8:
    print("Deberías tomar más agua.")
else:
    print("¡Buen trabajo con el consumo de agua!")