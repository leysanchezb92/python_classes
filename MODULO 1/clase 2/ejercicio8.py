# Pide el número de estudiantes en tres cursos y muestra el promedio de estudiantes por curso.

curso1=int(input("Ingrese el numero de estudiantes primer curso: "));
curso2=int(input("Ingrese el numero de estudiantes segundo curso: "));
curso3=int(input("Ingrese el numero de estudiantes tercer curso: "));

promedio = (curso1+curso2+curso3)/3;

print(f"El promedio de estudiantes por cuersos es {promedio}")