"""Uso de librería de fecha y tiempo"""

from datetime import datetime

str_date = "2/6/2024"

"""
d: día
m: mes
Y: año
"""

conversion = datetime.strptime(str_date, "%m/%d/%Y")
print(conversion)


"""Traer el mes de la fecha con foramto en letras: strftime de datime"""

conversion_mes = datetime.strftime(conversion, "%d %b del %Y")
print(conversion_mes)

"""
   b: reemplaza a 'm' para mostrar el mes de forma literal
"""
