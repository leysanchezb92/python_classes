#Crear una clase Circulo con un atributo de instancia radio y un atributo de clase pi. Añade un método para calcular el área.
import math

class Circulo:
    pi = 3.14159
    def __init__(self, radio):
        """
        Initialize Circle.

        Args:
            radio: Circle radius. (Ex: '10')
        """
        self.radio = radio

    def area_circulo(self):
        """
        Returns area.
        """
        area = math.pow(self.radio, 2) * self.pi
        return area

mi_circulo = Circulo(5)

print(f'El area del circulo es {mi_circulo.radio} es: {mi_circulo.area_circulo()}')