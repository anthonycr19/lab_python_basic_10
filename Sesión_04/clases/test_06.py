"""
POO en python
Encapsulamiento
"""

class A:
    def __init__(self):
        self.inicial = 10
        self._contador = 0  # Definiendo mi atributo privado

    def incrementa(self):
        self._contador = self._contador + 1

    def cuenta(self):
        return self._contador


class B:
    """Encapsulamiento"""
    def __init__(self):
        self.inicial = True
        self.__contador = 0 # Definiendo mi atributo privado

    def incrementa(self):
        self.__contador = self.__contador + 1

    def cuenta(self):
        return self.__contador


var_1 = A()
var_1._contador
var_1.inicial = 20

var_1.incrementa()
var_1.incrementa()

print(var_1.cuenta())
print("Valor inicial de A: {}".format(var_1.inicial))
print("Contador A: {}".format(var_1._contador))

var_2 = B()
var_2.inicial = False

var_2.incrementa()
var_2.incrementa()
var_2.incrementa()
var_2.incrementa()

print("Valor del contador B es: {}".format(var_2.cuenta()))
print("Valor de inicial B es: {}".format(var_2.inicial))


"""no es posible invocar a una variable porque su encapsulamiento es fuerte por los 2 guiones previos"""
print(var_2.__contador)
