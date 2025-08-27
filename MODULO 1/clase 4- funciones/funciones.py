programa1 = "Java de Cero a Senior"
programa2 = "Python con IA Aplicada"
programa3 = "Mobile Senior con IA"
valorProgramaBeca = 1800000
cantidad1 = 0
cantidad2 = 0
cantidad3 = 0

def mostrarMenu():
  print("\n ----MENU----")
  print("1. Mostrar los programas disponibles")
  print("2. Registrar la venta de cualquiera de los tres programas")
  print("3. Consultar los ingresos acumulados por cada programa")
  print("4. Mostrar el total general de ingresos del día")
  print("5. Salir del sistema")
  
def mostrarProgramas():
  print(f"1. {programa1} con un precio de {valorProgramaBeca}")
  print(f"2. {programa2} con un precio de {valorProgramaBeca}")
  print(f"3. {programa3} con un precio de {valorProgramaBeca}")
  
def ventaProducto():
  opcion = int(input("Ingrese el numero del producto que desea vender: "))
  
  if opcion == 1:
    cantidad = int(input(f"Cuantas matriculas desea realizar para el programa de {programa1}: "))
    total = cantidad * valorProgramaBeca
    print(f"Usted ha hecho la matricula de {cantidad} estudiantes de manera exitosa al {programa1}, por un valor de {total}")
  elif opcion == 2:
    cantidad = int(input(f"Cuantas matriculas desea realizar para el programa de {programa2}: "))
    total = cantidad * valorProgramaBeca
    print(f"Usted ha hecho la matricula de {cantidad} estudiantes de manera exitosa al {programa2}, por un valor de {total}")
  elif opcion == 3:
    cantidad = int(input(f"Cuantas matriculas desea realizar para el programa de {programa3}: "))
    total = cantidad * valorProgramaBeca
    print(f"Usted ha hecho la matricula de {cantidad} estudiantes de manera exitosa al {programa3}, por un valor de {total}") 
  else:
    print("Opcion invalida")

while True:
  mostrarMenu()
  opcion = int(input("Seleccione una opcion: "))
  
  if opcion == 1:
    mostrarProgramas()
  elif opcion == 2:
    mostrarProgramas()
    ventaProducto()
  elif opcion == 5:
    print("Vuelva pronto")
    break