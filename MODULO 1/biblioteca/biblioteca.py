from prettytable import PrettyTable

libros = [
  {
    'isbn': '978-0321765723',
    'titulo': 'El Señor de los Anillos',
    'autor': 'J.R.R. Tolkien',
    'estado': 'Disponible',
    'socio_prestado': None
  },
  {
    'isbn': '978-0743273565',
    'titulo': 'Cien años de soledad',
    'autor': 'Gabriel García Márquez',
    'estado': 'Disponible',
    'socio_prestado': None
  },
  {
    'isbn': '978-0451524935',
    'titulo': '1984',
    'autor': 'George Orwell',
    'estado': 'Disponible',
    'socio_prestado': None
  },
  {
    'isbn': '978-0743273565',
    'titulo': 'Orgullo y prejuicio',
    'autor': 'Jane Austen',
    'estado': 'Disponible',
    'socio_prestado': None
  },
  {
    'isbn': '978-0743273565',
    'titulo': 'Don Quijote de la Mancha',
    'autor': 'Miguel de Cervantes',
    'estado': 'Prestado',
    'socio_prestado': 'Juan Pérez'
  },
  {
    'isbn': '978-0061120084',
    'titulo': 'Matar un ruiseñor',
    'autor': 'Harper Lee',
    'estado': 'Disponible',
    'socio_prestado': None
  },
  {
    'isbn': '978-0385504201',
    'titulo': 'El Código Da Vinci',
    'autor': 'Dan Brown',
    'estado': 'Prestado',
    'socio_prestado': 'María López'
  },
  {
    'isbn': '978-0439023528',
    'titulo': 'Harry Potter y la piedra filosofal',
    'autor': 'J.K. Rowling',
    'estado': 'Disponible',
    'socio_prestado': None
  },
  {
    'isbn': '978-0345339683',
    'titulo': 'Dune',
    'autor': 'Frank Herbert',
    'estado': 'Disponible',
    'socio_prestado': None
  },
  {
    'isbn': '978-0307593313',
    'titulo': 'Los juegos del hambre',
    'autor': 'Suzanne Collins',
    'estado': 'Disponible',
    'socio_prestado': None
  }
]
socios = [
  {
    'id': 101,
    'nombre': 'Juan',
    'apellido': 'Pérez',
    'estado': 'Activo',
    'socio_prestamos': None
  },
  {
    'id': 102,
    'nombre': 'María',
    'apellido': 'Gómez',
    'estado': 'Activo',
    'socio_prestamos': None
  },
  {
    'id': 103,
    'nombre': 'Carlos',
    'apellido': 'Rodríguez',
    'estado': 'Inactivo',
    'socio_prestamos': None
  },
  {
    'id': 104,
    'nombre': 'Ana',
    'apellido': 'Martínez',
    'estado': 'Activo',
    'socio_prestamos': None
  },
  {
    'id': 105,
    'nombre': 'Luis',
    'apellido': 'Hernández',
    'estado': 'Activo',
    'socio_prestamos': None
  },
  {
    'id': 106,
    'nombre': 'Sofía',
    'apellido': 'Díaz',
    'estado': 'Activo',
    'socio_prestamos': None
  },
  {
    'id': 107,
    'nombre': 'Pedro',
    'apellido': 'Sánchez',
    'estado': 'Inactivo',
    'socio_prestamos': None
  },
  {
    'id': 108,
    'nombre': 'Laura',
    'apellido': 'Ramírez',
    'estado': 'Activo',
    'socio_prestamos': None
  },
  {
    'id': 109,
    'nombre': 'Diego',
    'apellido': 'Torres',
    'estado': 'Activo',
    'socio_prestamos': None
  },
  {
    'id': 110,
    'nombre': 'Valeria',
    'apellido': 'Flores',
    'estado': 'Activo',
    'socio_prestamos': None
  }
]

contador = 1

def mostrar_menu():
  print(" ------------MINIBIBLIOTECA------------- ")
  print(" 1. Registrar Libro")
  print(" 2. Registrar un socio")
  print(" 3. Prestar un libro")
  print(" 4. Devolver libro")
  print(" 5. Ver libros prestados")
  print(" 6. Ver todos los libros")
  print(" 7. Ver todos los socios")
  print(" 0. Salir")
  
def registrar_libro():
  global libros
  print("Registrar libro: ")
  
  titulo = input("Titulo del libro: ").strip().lower()
  if titulo == '0': return
  if not titulo:
    print("El titulo no puede estar vacio.")
    return
    
  autor = input("autor del libro: ").strip().lower()
  if autor == '0': return
  if not autor:
    print("El autor no puede estar vacio.")
    return
    
  isbn = input("ISBN del libro").strip().lower()
  if isbn == '0': return
  if not isbn:
    print("El ISBN no puede estar vacio")
    return
  
  for libro in libros:
    if libro['isbn'] == isbn:
      print(f"Ya existe un libro con ese ISBN {isbn}")  
      
  
  nuevo_libro = {
    'isb': isbn,
    'titulo': titulo,
    'autor': autor,
    'estado': 'Disponible',
    'socio_prestado': None
  }
  
  libros.append(nuevo_libro)
  print("Libro registrado exitosamente")
  

def registrar_socio():
  global socios
  
  idSocio = input("ID del socio: ")
  if idSocio == '0': return
  if not idSocio:
    print("El ID no puede estar vacio.")
    return
  
  nombre = input("Nombre del socio: ").strip().lower()
  if nombre == '0': return
  if not nombre:
    print("El nombre no puede estar vacio.")
    return
  
  apellido = input("Apellido del socio: ").strip().lower()
  if apellido == '0': return
  if not apellido:
    print("El apellido no puede estar vacio.")
    return
  
  for socio in socios:
    if socio['idSocio'] == idSocio:
      print(f"Ya existe el documento {idSocio}")  
      
  
  nuevo_socio = {
    'id': idSocio,
    'nombre': nombre,
    'apellido': apellido,
    'estado': 'Activo',
    'socio_prestamos': None
  }
  
  socios.append(nuevo_socio)
  print("Se ha registrado correctamente el socio")

def prestar_libro():
  global libros, socios
  pass

def devolver_libro():
  pass

def ver_libro_prestado():
  pass

def ver_todos_libros():
  table = PrettyTable()
  table.field_names = ["Titulo", "Autor", "ISBN", "Estado"]
  
  for libro in libros:
    table.add_row([libro['titulo'], libro['autor'], libro['isbn'], libro['estado']])
  
  print(table)

def ver_todos_socio():
  table = PrettyTable()
  table.field_names = ["ID Socio", "Nombre", "Apellido", "Estado", "Prestamos"]
  
  for socio in socios:
    table.add_row([socio['id'], socio['nombre'], socio['apellido'], socio['estado'], socio['socio_prestamos']])
  
  print(table)
  
def main():
  while True:
    mostrar_menu()
    # Usas .strip() correctamente para evitar errores por espacios accidentales
    opcion = input("Ingrese la opcion de 0 a 7: ").strip()
    
    match opcion:
      case "1":
          registrar_libro()
      case "2":
          registrar_socio()
      case "3" | "4" | "5": # Puedes agrupar casos si aún no tienen lógica
          print("Funcionalidad en desarrollo...")
      case "6":
          print("\n--- Todos los libros que tenemos ---")
          ver_todos_libros()
      case "7":
          print("\n--- Todos los socios registrados ---")
          ver_todos_socio()
      case "0":
          print("Ha cerrado sesión con éxito. ¡Hasta pronto!")
          break
      case _: # IMPORTANTE: Maneja entradas incorrectas
          print("Opción no válida. Por favor, ingrese un número del 0 al 7.")

# ¡No olvides llamar a la función para que el programa inicie!
if __name__ == "__main__":
    main()
      
print(main())