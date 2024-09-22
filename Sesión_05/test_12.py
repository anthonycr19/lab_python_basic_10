"""
    Decoradores en Python
"""
"""Creación interna de la función decoradora"""


def funcionADecoradora(funcionB):
    def funcionC(*args, **kwargs):
        print("1. Antes de ejecutar la función a decorar")
        resultado = funcionB(*args, **kwargs)
        print("2. Después de ejecutar la función a decorar")
        return resultado
    return funcionC


@funcionADecoradora
def saludar(nombre, apellido, edad, **kwargs):
    print("Hola {} {}, usted tiene {} años".format(nombre, apellido, edad))
    for key, value in kwargs.items():
        print("{} = {}".format(key, value))


saludar("Julio", "Gutierrez", 29, ciudad1="Lima",
        ciudad2="Tacna", ciudad3="Arequipa")
