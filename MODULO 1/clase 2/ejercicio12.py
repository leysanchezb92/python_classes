# Pide el número de empleados de dos sucursales y muestra cuál tiene más personal.

empleadosSucursal1= int(input("Ingrese el numero de empleados en la primera sucursal: "));
empleadosSucursal2= int(input("Ingrese el numero de empleados en la segunda sucursal: "));

if empleadosSucursal1 > empleadosSucursal2:
  print(f"la primera sucursarl cuenta con más empleados que la segunda");
elif empleadosSucursal1 < empleadosSucursal2:
  print(f"la segunda sucursarl cuenta con más empleados que la primera");
