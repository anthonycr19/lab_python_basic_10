"""
    Decoradores en Python
"""

"""
  Función decoradora que valida los argumentos
  que se pasan a una función antes que se ejecute
"""


def validar_param_positivo(func):
    def funcB(*args):
        print("1. Evaluando parámetros...")
        for arg in args:
            if arg < 0:
                print("Todos los elementos deben ser positivos")

        print("Los parámetros están correctos, se ejecuta la función...")
        resultado = func(*args)
        print("2. Se ejecutó la función y su resultado es: {}"
              .format(resultado))
        return resultado
    return funcB


@validar_param_positivo
def multipl(a, b, c):
    return a*b*c


# Llamada de prueba
multipl(4, 10, 7.3)
multipl(2, 6, 8)
multipl(1, 3, 5)
