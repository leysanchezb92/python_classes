# Pide el nombre de un proyecto y los días estimados de duración, luego muestra cuántas semanas tomará (redondeando hacia arriba).

import math

nombreProyecto = input("Ingresa el nombre del proyecto: ");
duracionDiasProyecto = int(input("Ingrese el número de días estimado de duración del proyecto: "));semanas = math.ceil(duracionDiasProyecto / 6);

print(f"El proyecto {nombreProyecto} esta presupuestado para durar {semanas} semanas.");


