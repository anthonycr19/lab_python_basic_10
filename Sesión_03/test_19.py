"""Asignación múltiple"""
"""Referencia a dos o más variables con sus respectivos datos"""

var1 = input("Ingrese nombre de usuario: ")
var2 = input("Ingrese nombre: ")
var3 = input("Ingrese su edad: ")

#usuario = var1
#nombre = var2
#edad = var3

usuario, nombre, edad = var1, var2, var3

print("Su nombre de usuario es: {} y tiene {} años".format(usuario, edad))
