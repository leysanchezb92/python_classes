# Solicita la cantidad de productos vendidos y el precio unitario, luego muestra el total de ventas.
import math
productosVendidos=int(input("Ingrese la cantidad de productos vendidos: "));
precioUnitario = float(input("Ingrese el precio unitario: "));
precioUnitario *= productosVendidos

print(f"Total de ventas {math.ceil(precioUnitario)}");