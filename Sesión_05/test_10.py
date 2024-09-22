"""Uso de la librería JSONn para tratar tipo de datos JSON"""
import json

"""Uso de la librería JSON"""

data_python = {'nombre': 'Milagros', 'edad': 32, 'distrito': 'Jesús María'}

"""Convirtiendo a un dato tipo Json: dumps()"""
data_python_to_json = json.dumps(data_python)

print(data_python_to_json)
print(type(data_python_to_json))
