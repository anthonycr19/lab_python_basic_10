"""Programación funcional con Python"""

var_1 = 80
var_2 = 180

"""Input: dos variables que pasarán por parámetro de la función"""
"""a,b: parámetros de la función 'sumar'"""


def sumar(a, b):
    return a + b


"""

def sumar(a, b):
    suma = a + b
    var_1 = pow(suma, 3)
    return var_1
"""

resultado = sumar(var_1, var_2)
"""Output: lo que retorna la función"""
print(resultado)

resultado_2 = sumar(90.7, 150.90)
print(resultado_2)
