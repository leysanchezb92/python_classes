# Crear una clase Empleado y una clase Gerente que herede de Empleado. El gerente debe tener un atributo adicional departamento.

class Empleado:
    def __init__(self, nombre, apellido, identificacion ):
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        pass

class Gerente(Empleado):
    def __init__(self, departamento):
        self.departamento = departamento
        super().__init__()
        pass