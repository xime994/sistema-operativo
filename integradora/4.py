aprobados = 0
desaprobados = 0

for i in range(10):
    nota = float(input(f"Ingresá la nota del alumno {i+1}: "))
    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1

print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")