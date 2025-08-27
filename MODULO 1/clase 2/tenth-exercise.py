# Una empresa desea calcular el Retorno sobre la Inversión (ROI) y verificar si la inversión fue rentable (mayor a 1).

costo_inversion = int(input("ingrese el valor costo de inversion: "))
ingreso_obtenido = int(input("ingrese el ingreso obtenido: "))
beneficio = ingreso_obtenido - costo_inversion;
rentabilidad = (beneficio/costo_inversion)
roi = (beneficio/costo_inversion)*100

print(f"la inversion fue {rentabilidad>1} rentable");
print(f"el retorno de la inversion fue de {roi}");