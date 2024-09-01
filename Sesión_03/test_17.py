"""Entrada y salida en Python"""

usuario = input("Ingrese su usuario: ")
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

print("Su usuario es: {}".format(usuario))
print("Bienvenido/a {}".format(nombre))

actualizar = int(edad) + 5
print("Su edad actualizada es: {} años".format(actualizar))
