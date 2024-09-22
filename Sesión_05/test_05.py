"""Uso de librería de fecha y tiempo"""

from datetime import datetime, date

fecha = date.today()
print(fecha)

tiempo = datetime.now()
print(tiempo)

anio = tiempo.year
mes = tiempo.month
dia = tiempo.day

print("Año actual: {}".format(anio))
print("Mes actual: {}".format(mes))
print("Día actual: {}".format(dia))

"""Uso de datetime para extraer la hora, el minuto y el segundo actual"""
hora = tiempo.hour
minuto = tiempo.minute
segundo = tiempo.second

print("Hora actual: {}".format(hora))
print("Minuto actual: {}".format(minuto))
print("Segundo actual: {}".format(segundo))
