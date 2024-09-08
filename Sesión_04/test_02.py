"""Uso del flujo condicional 'if'"""

edad1 = int(input("Ingrese una primera edad "))
edad2 = int(input("Ingrese una segunda edad "))

if edad1 > edad2:
    print("La edad 1 es mayor que la edad 2 que ha ingresado")
elif edad1 == edad2:
    print("Las edades ingresadas son iguales")
else:
    print("La edad 2 es mayor que la edad 1 que ha ingresado")
