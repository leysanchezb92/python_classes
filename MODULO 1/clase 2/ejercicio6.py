# Pide la edad de un usuario y muestra si puede acceder a un sistema restringido para mayores de 21 años.

edad = int(input("Ingrese su edad: "))

if edad < 21: 
  print("No puede ingresar");
else:
  print("Ingrese por favor");