# Crear una clase Coche con atributos para marca, modelo y año. Incluye un método para mostrar su información.

class Coche():
	"""Clase base para todo tipo de vehiculo"""
	def __init__(self, marca: str, modelo: str, anio: int):
		"""
		Inicializa un vehiculo.

		Args:
			marca (str): El marca del carro. (Ej: 'Toyota)
			modelo (str): Modelo del carro. (Ej: 'Corolla')
			anio (int): Año de fabricacion. (Ej: 2001)
		"""
		self.marca = marca
		self.modelo = modelo
		self.anio = anio

	def mostrar_info(self):
		"""
		Método para imprimir la informacion del vehiculo.
        Cada subclase del coche debe implementar mostrar informacion.
        """
		print(f'la marca del carro es: {self.marca}, su modelo es: {self.modelo} y su año es {self.anio}.')

mi_coche = Coche('Mercedes Benz', 'Kompressor', 2005)
print(mi_coche.mostrar_info())

		