# Crear una clase Estudiante con nombre, edad y una lista de calificaciones. Implementa el método **str** para una representación legible.

class Students():
    def __init__(self, name: str, age: int, grades: list):
        """
		Initialize Students.

		Args:
			name (str): Students name (Ex: 'Pedro')
			age (int): Students age. (Ex: '10')
            grades(list): Student grades a list of floats or integers. (Ex: [4.5,3,4])
		"""
        self.name = name
        self.age = age
        self.grades = grades

    def __str__(self):
        """
        Returns a string representation of the student.
        """
        cadena = f"('Student: {self.name} with age: {self.age} and the grades are: {self.grades}')"
        return cadena

student1 = Students(name="Ana", age=22, grades=[95, 88, 92])
print(student1)