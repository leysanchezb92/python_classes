# Crear una clase Animal con un método hacer_sonido(). Crear clases Perro y Gato que hereden y sobrescriban este método.

class Animal:
    def __init__(self, nombre: str, especie: str, edad: int):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def hacer_sonido(self):
        print(f'el {self.nombre} hace un sonido de grrr')

class Perro(Animal):
    def init(self, nombre: str, especie: str, edad: int, raza: str):
        super().__init__(nombre, especie, edad)
        self.raza = raza

    def hacer_sonido(self):
        print(f'el perro {self.nombre} tienen una edad de {self.edad} y hace guau guau')

perro1 = Perro('mojito', 'perro', 3, 'border collie')

# Just call the method directly.
perro1.hacer_sonido()