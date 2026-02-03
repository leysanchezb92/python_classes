class Habitacion:
    def __init__(self, numero: int, tipo: str):
        self.numero = numero
        self.tipo = tipo
        self.disponible = True

    def reservar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True
    
    def consultar_perfil(self):
        estado = "Disponible" if self.disponible else "No disponible"
        print(f'Habitación {self.numero} - Tipo: {self.tipo} - Estado: {estado}')

class Hotel:
    def __init__(self, nombre_hotel: str, habitaciones: list[Habitacion]):
        self.nombre_hotel = nombre_hotel
        self.habitaciones = habitaciones

    def mostrar_disponibilidad(self):
        print(f'\n--- Disponibilidad en el hotel {self.nombre_hotel} ---')
        for habitacion in self.habitaciones:
            habitacion.consultar_perfil()
    
class Usuario:
    def __init__(self, id_usuario: str, nombre: str):
        self.id_usuario = id_usuario
        self.nombre = nombre

    def actualizar_datos(self):
        new_name = input(f'Ingrese nuevos datos para {self.nombre}: ')
        self.nombre = new_name
        return f'Datos actualizados correctamente. Usuario: {self.nombre}'

    def consultar_datos(self):
        return f'ID Usuario: {self.id_usuario}, Nombre: {self.nombre}'
    
class Administrador(Usuario):
    def __init__(self, id_usuario: str, nombre: str, rol: str, hoteles: list[Hotel]):
        super().__init__(id_usuario, nombre)
        self.rol = rol
        self.hoteles = hoteles

    def registrar_habitacion(self):
        if self.rol != 'Gestor de Habitaciones':
            return 'No tiene permisos para registrar habitaciones.'
        try:
            numero = int(input('Ingrese el número de la nueva habitación: '))
            tipo = input('Ingrese el tipo de habitación: ')
            nueva_habitacion = Habitacion(numero, tipo)
            self.hoteles[0].habitaciones.append(nueva_habitacion)
            return f'Habitación {numero} registrada exitosamente.'
        except ValueError:
            return "Error: El número de habitación debe ser un entero."

class Prestamo:
    def __init__(self, id_prestamo: str, id_usuario: str, id_habitacion: int, fecha_inicio: str, fecha_fin: str):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.id_habitacion = id_habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def registrar_reserva(self, hotel: Hotel, administradores: list[Administrador]):
        # Buscamos si hay un administrador con el rol correcto
        admin_autorizado = next((a for a in administradores if a.rol == 'Gestor de Reservas'), None)
        
        if not admin_autorizado:
            return 'Error: No hay un administrador con rol "Gestor de Reservas" para autorizar.'

        for hab in hotel.habitaciones:
            if hab.numero == self.id_habitacion:
                if hab.disponible:
                    hab.reservar()
                    return f'Reserva {self.id_prestamo} confirmada por {admin_autorizado.nombre}.'
                else:
                    return f'La habitación {self.id_habitacion} ya está ocupada.'
        return 'Habitación no encontrada en el hotel.'

class Cliente(Usuario):
    def __init__(self, id_usuario: str, nombre: str, numero_celular: str, correo: str, prestamos=None):
        super().__init__(id_usuario, nombre)
        self.numero_celular = numero_celular
        self.correo = correo
        self.prestamos = prestamos if prestamos else []

    def consultar_perfil(self):
        prestamos_info = ', '.join([p.id_prestamo for p in self.prestamos]) if self.prestamos else "Ninguno"
        return (f'PERFIL CLIENTE - ID: {self.id_usuario}, Nombre: {self.nombre}, '
                f'Celular: {self.numero_celular}, Correo: {self.correo}, Préstamos: {prestamos_info}')

    def consultar_prestamos(self):
        if self.prestamos:
            return f'Préstamos activos de {self.nombre}: ' + ', '.join([p.id_prestamo for p in self.prestamos])
        return f'{self.nombre} no tiene préstamos activos.'

# Ejemplo de uso corregido
if __name__ == "__main__":
    # 1. Preparar infraestructura
    h1 = Habitacion(101, 'Individual')
    h2 = Habitacion(102, 'Doble')
    mi_hotel = Hotel('Loira Central', [h1, h2])

    # 2. Crear personal
    admin_res = Administrador('A01', 'Carlos', 'Gestor de Reservas', [mi_hotel])
    admin_hab = Administrador('A02', 'Ana', 'Gestor de Habitaciones', [mi_hotel])

    # 3. Crear cliente
    cliente1 = Cliente('C01', 'Luis', '3001234567', 'luis@email.com')

    # 4. Proceso de Reserva
    print(cliente1.consultar_perfil())
    
    # Creamos un objeto préstamo (reserva)
    nueva_reserva = Prestamo('R-001', cliente1.id_usuario, 101, '2024-02-01', '2024-02-05')
    
    # Intentamos registrarla
    resultado = nueva_reserva.registrar_reserva(mi_hotel, [admin_res])
    print(resultado)
    
    if "confirmada" in resultado:
        cliente1.prestamos.append(nueva_reserva)

    # 5. Ver resultados
    mi_hotel.mostrar_disponibilidad()
    print(cliente1.consultar_prestamos())