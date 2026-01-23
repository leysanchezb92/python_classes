# Crear una clase Empleado y una clase Gerente que herede de Empleado. El gerente debe tener un atributo adicional departamento.

class Empleado:
    def __init__(self, nombre, apellido, identificacion ):
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion


class Gerente(Empleado):
    def __init__(self, departamento, nombre, apellido, identificacion):
        super().__init__(nombre, apellido, identificacion)
        self.departamento = departamento
    

empleado1 = Empleado("Carlos", "Lopez", "12345678")
gerente1 = Gerente("Ventas", "Ana", "Gomez", "87654321")

print(f'Empleado: {empleado1.nombre} {empleado1.apellido}, ID: {empleado1.identificacion}')
print(f'Gerente: {gerente1.nombre} {gerente1.apellido}, ID: {gerente1.identificacion}, Departamento: {gerente1.departamento}')
