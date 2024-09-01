"""Diccionarios en Python"""

"""del: elimina un key y valor del diccionario"""

var_1 = {"nombre": "Matías", "edad": 26, "promedio": 14}

"""Para eleiminar valores de nuestro diccionario usamos a del, delanete de la varaible"""

var_1["distrito"] = "Lince"
del var_1["edad"]
del var_1["promedio"]

print("El diccionario actualizado tiene los siguientes valores: {}".format(var_1))
