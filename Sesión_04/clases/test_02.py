"""
    Programación Orientada a Objetos
"""


class Carro:
    """Atributos"""
    ruedas = 4

    """Constructor: Valores que van a tener por defecto mi clase que se le instancia a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: Son las funciones de las clase"""
    def acelerar(self):
        self.velocidad = self.velocidad - self.aceleracion

    def frenar(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0

        self.velocidad = velocidad


carro_1 = Carro("Blanco", 60)
print("El color de mi primer carro es: {}".format(carro_1.color))

carro_2 = Carro("Rojo", 80)
carro_2.marchas = 30000

print("El número de marchas de mi segundo carro es: {}".format(carro_2.marchas))


"""Importante"""
"""No es posible llamar un atributo de datos que se le ha asigando a otra instanacia de la clase"""
#print(carro_1.marchas)
