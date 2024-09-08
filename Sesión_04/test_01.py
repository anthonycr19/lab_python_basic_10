"""Uso del condificional: if"""

edad = int(input("¿Cuál es su edad? "))

if 0 < edad < 18:
    print("Usted es menor de edad")
elif 18 <= edad < 65:
    print("Usted es una persona adulta")
elif 65 <= edad <= 100:
    print("Usted es una persona adulta de la tercera edad")
else:
    print("Usted ha ingresado una edad incorrecta, ingrese una edad correcta por favor")
