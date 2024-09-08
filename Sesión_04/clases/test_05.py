"""
    Programación Orientada a Objetos
    Participación

Requerimientos:
    - Crear una Clase Alumno
    - Debe tener un atributo de nacionalidad con el valor "Peruano"
    - Crear un método que indicará el promedio del alumno
    - Crear un método que indicará si el alumno está aprobado o no de acuerdo a su promedio
    - Tendrá 3 notas, la nota inicial de c/u será de 0
    - Las notas serán pasadas por parámetro al momento de instanciar la clase
    - Método para ontener el nombre y distrito de residencia del alumno
    - Instanciar la clase para el caso de 2 alumnos.
"""

class Alumno:

    def __init__(self, nota_1, nota_2, nota_3):
        self.nacionalidad = "Peruano"
        self.nota_1 = 0
        self.nota_2 = 0
        self.nota_3 = 0

    def promedio(self):
        pass

    def aprobado(self):
        pass


alumno_1 = Alumno()
alumno_2 = Alumno()
