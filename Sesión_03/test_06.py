"""Listas en Python"""

"""Listas (count): Cantidad de veces que aparece el elemento que se repite en una lista"""

var_1 = ["Python", "Java", "PHP", "Javascript", "Typescript"]

var_1.append("Python")
var_1.append("Python")
var_1.append("python")
var_1.append("Python")
var_1.append("NodeJS")

print("Mi lista actualizada tiene los siguiente valores: {}".format(var_1))

print("La cantidad de veces que se repite 'Python' es: {}".format(var_1.count("Python")))
print("La cantidad de veces que se repite 'Java' es: {}".format(var_1.count("Java")))
