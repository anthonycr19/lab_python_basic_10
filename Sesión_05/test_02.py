"""Controlo o gestión de exepciones"""

"""
TypeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
ImportError
OverFlowError

"""
"""Estructura y uso"""
"""
try:
    bloque código 1
except 'exepción 1'
    bloque código 2
else:
    bloque código 3
"""


def division(a, b):
    try:
        resultado = a/b
        print("División correcta")
    except ZeroDivisionError:
        print("¡No es posible dividir estos valores!")
        resultado = None
        print("Resultado: {}".format(resultado))
    else:
        print("Resultado: {}".format(resultado))


division(1000, 5)
division(400, 0)
division(2, 500)
