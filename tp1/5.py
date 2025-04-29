numero = int(input("Ingrese un número entero entre 0 y 10 (ambos inclusive): "))

if 0 <= numero <= 10:
  if numero % 2 == 0:
    print(f"El número {numero} es par.")
  else:
    print(f"El número {numero} es impar.")
else:
  print(" El número ingresado no es valido.")