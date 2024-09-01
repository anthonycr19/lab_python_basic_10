"""Listas en Python"""

"""Listas (copy): Obtenemos todos los valores de una lista en otra variable"""

var_1 = ["sQLServer", "rDS", "MYSQL", "Postgresql", "MariaDB"]

var_2 = var_1.copy()

print("El valor de mi var_2 es: {}".format(var_2))

var_2.append("SQLite3")
print("El valor de mi var_2 es: {}".format(var_2))

print("Los valores de mi var_1 son: {}".format(var_1))
