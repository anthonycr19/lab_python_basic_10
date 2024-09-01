"""Diccionarios en Python"""

"""Los nombre de los key(llaves) van a ir escritos siempre en minúsculas (Por convención)"""

var_1 = {"nombre": "Matías", "edad": 26, "promedio": 14}

print("Nuestro diccionario tiene el siguiente contenido: {}".format(var_1))

"""Agregamos elementos en nuevo key a mi diccionario"""

var_1["distrito"] = "San Isidro"
var_1["habilitado"] = True
var_1["nombre"] = "Fiorella"

print("Mi diccionario actualizado tiene los siguiente valores: {}".format(var_1))
