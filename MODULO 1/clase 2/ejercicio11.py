# Solicita el puntaje de dos exámenes y muestra si el estudiante mejoró, empeoró o mantuvo su rendimiento.

primerExamen = float(input("Ingrese el puntaje del primer examen: "));
segundoExamen = float(input("Ingrese el puntaje del segundo examen: "));

if segundoExamen > primerExamen:
  print("El estudiante ha mejorado rendimiento");
elif segundoExamen == primerExamen:
  print("El estudiante ha mantenido su rendimiento");
else:
  print("El estudiante ha empeorado su rendimiento");
