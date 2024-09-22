"""Uso de librería de fecha y tiempo
Conversión de fechas
"""
import datetime

fecha1 = datetime.datetime(2024, 4, 23)
fecha2 = datetime.datetime(2024, 4, 20)

if fecha1 == fecha2:
    print("Nacieron el mismo día")
elif fecha1 > fecha2:
    print("El niño 2 es mayor que el niño 1")
else:
    print("El niño 1 es mayor que el niño 2")
