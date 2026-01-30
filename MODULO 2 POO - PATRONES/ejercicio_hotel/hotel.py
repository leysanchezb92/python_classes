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
        print(f'Disponibilidad en el hotel {self.nombre_hotel}:')
        for habitacion in self.habitaciones:
            habitacion.consultar_perfil()
    

class Usuario:
    def __init__(self, id_usuario: str, nombre: str):
        self.id_usuario = id_usuario
        self.nombre = nombre

    def actualizar_datos(self):
        new_name = input('Ingrese nuevos datos: ')
        self.nombre = new_name
        return f'Datos actualizados correctamente. Usuario: {self.nombre}'

    def consultar_datos(self):
        return f'ID Usuario: {self.id_usuario}, Nombre: {self.nombre}'
    
class Administrador(Usuario):
    def __init__(self, id_usuario: str, nombre: str, rol: str):
        super().__init__(id_usuario, nombre)
        self.rol = rol

    def registrar_habitacion(self):
        pass

    def eliminar_prestamo(self):
        pass
        
class Cliente(Usuario):
    def __init__(self, id_usuario: str, nombre: str, numero_celular: str, correo: str, prestamos: list[Prestamo]):
        super().__init__(id_usuario, nombre)
        self.numero_celular = numero_celular
        self.correo = correo
        self.prestamos = prestamos

    def consultar_perfil(self):
        return f'ID Usuario: {self.id_usuario}, Nombre: {self.nombre}, Celular: {self.numero_celular}, Correo: {self.correo}'

    def consultar_prestamos(self):
        pass
        
    
class Prestamo:
    def __init__(self, id_prestamo: str, id_usuario: str, id_habitacion: str, fecha_inicio: str, fecha_fin: str, habitaciones: list[Habitacion], administrador: list[Administrador]):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.id_habitacion = id_habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.habitaciones = habitaciones
        self.administrador = administrador

    def registrar_prestamo(self, habitaciones: list[Habitacion], administrador: list[Administrador]):
        for admin in administrador:
            print(f'Administrador {admin.nombre} está gestionando la reserva...')
            if admin.rol == 'Gestor de Reservas':
                print(f'Administrador {admin.nombre} tiene el rol adecuado para gestionar reservas.')
                for habitacion in habitaciones:
                    print(f'Intentando reservar habitación {habitacion.numero}...')
                    if habitacion.disponible:
                        habitacion.reservar()
                        self.habitaciones.append(habitacion)
                        return f'Habitación {habitacion.numero} reservada exitosamente.'
                return f'Habitación {habitacion.numero} no está disponible.'
            else:
                print(f'Administrador {admin.nombre} no tiene el rol adecuado para gestionar reservas.')
        return 'No se pudo completar la reserva debido a la falta de un administrador con el rol adecuado.'

    def eliminar_prestamo(self, habitaciones: list[Habitacion], administrador: list[Administrador]):
        for admin in administrador:
            if admin.rol == 'Gestor de Reservas':
                print(f'Administrador {admin.nombre} tiene el rol adecuado para gestionar reservas.')
                for habitacion in habitaciones:
                    numero_habitacion = int(input('Ingrese el numero de habitacion para cancelar reserva: '))
                    if habitacion.numero == numero_habitacion and habitacion.disponible == False:
                        habitacion.disponible = True
                        print(f'Fue cancelada la reservacion de la habitacion numero {habitacion.numero}, ahora esta disponible')
            else:
                print(f'Administrador {admin.nombre} no tiene el rol adecuado para gestionar reservas.')
        return f'No se encontro la habitacion numero {numero_habitacion} en los prestamos activos.'

        

