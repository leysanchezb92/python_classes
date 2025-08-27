# Solicita el número de libros prestados y el número de libros devueltos en una biblioteca, luego muestra cuántos libros quedan prestados.

librosPrestado = int(input("Ingresa el numero de libros prestados: "))
librosDevueltos = int(input("Ingresa el numero de libros devueltos: "))
librosFaltantes = librosPrestado - librosDevueltos

if librosFaltantes > 0:
  print(f"Recuerda que aún tienes {librosFaltantes} libros por entregar")
