# Pide el nombre de un cliente y el monto de su compra, luego muestra si aplica a un descuento (si la compra es mayor a $500.000).

nombreCliente = input("Ingrese el nombre del cliente: ")
montoCompra= int(input(f"Ingrese el monto que compro {nombreCliente}: "))

if montoCompra >= 500000:
  valorTotal= montoCompra - (montoCompra * 0.2)
  print(f"{nombreCliente} tiene un descuento del 20% en su compra, ahora el valor a pagar es {valorTotal}")
elif montoCompra < 500000:
  print(f"{nombreCliente} no tiene descuentos disponibles")