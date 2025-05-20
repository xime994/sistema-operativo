sueldo=float(input("Ingrese su sueldo:"))
if sueldo < 1000:
    sueldo=sueldo+(sueldo*0.15)
    print("Su sueldo ahora es de:",sueldo)
else:
    print("Su sueldo queda igual")