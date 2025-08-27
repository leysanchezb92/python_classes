# Solicita el nombre de un estudiante y su nota final. Muestra si aprobó el curso (nota ≥ 3.0).

nombreEstudiante=input("Ingrese nombre del estudiante: ")
notaFinal=int(input("Ingreso nota final: "))

if notaFinal >= 3:
  print(f"El estudiante aprobo")
else:
  print(f"El estudiante reaprobo")
  