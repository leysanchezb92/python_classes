# Solicita la cantidad de materias inscritas por un estudiante y muestra si tiene sobrecarga académica (más de 7 materias).

cantidadMaterias = int(input("Ingrese la cantidad de materios a tomar este semestre: "))

if cantidadMaterias > 7:
  print("Tiene una sobrecarga academica, considere la cantidad de materias escritas.")
elif cantidadMaterias < 7:
  print("Exitos en este semestre")