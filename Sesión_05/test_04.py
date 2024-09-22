"""Control o gestión de exepciones"""

"""
    - Crear una función aplicando exepciones donde el bloque del except
    va a considerar a los errors de división entre cero y el tipo de error
    - Los valores tienen que ser ingresados por consola
"""

"""
-Agregar un exepción donde se va a considerar una lista
con 4 valores, todos sus datos serán string
-Al querer modificar una de las posiciones no existentes
crear un nuevo índice y darle valor de "0"
-Mostrar la lista final
"""


def addValue(val1, val2):
    try:
        val1[val2] = "0"
        print(val1)
    except IndexError:
        val1.append("0")
        print(val1)


values = ["a", "b", "c", "d"]
i = 4
addValue(values, i)
