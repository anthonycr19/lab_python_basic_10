"""Uso del bucle While"""

numero = int(input("¿Cuántos saludos desea enviar?: "))

while numero < 10:
    print(numero)
    numero = numero + 1
    # El número ya aumento un valor
    print("Número con nuevo valor: {}".format(numero))
