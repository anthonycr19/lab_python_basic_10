"""Listas en Python"""

"""Listas (del): Eliminar un valor indicando el índice del valor de la lista"""

paises = []
paises.append("Perú")
paises.append("Brasil")
paises.append("Argentina")
paises.append("Canadá")
paises.append("España")
paises.append("Colombia")

print("Los valores de mi lista son: {}".format(paises))

del paises[2]
del paises[4]

print("Mi lista actualizada tiene los siguiente valores: {}".format(paises))
