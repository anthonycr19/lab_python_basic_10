"""Controlo o gestión de exepciones"""

"""
    Crear una aplicación usando exepciones donde no se pueda
    realizar la suma entre diferentes tipos de datos
"""


def operaciones(a, b):

    try:
        # resultado = a + b
        resultado = a/b
    except TypeError:
        print("No se puede sumar un string con un dato int")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    else:
        print(resultado)


operaciones(40, "Lima")
operaciones(40, 0)
