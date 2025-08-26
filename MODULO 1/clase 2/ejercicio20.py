# Pide el número de participantes en un evento y muestra si se superó el cupo máximo de 100 personas.
participantes = int(input("ingrese el numero de participantes: "));

if participantes <= 100:
  print(f"El numero de participantes que tiene es de {participantes}")
elif participantes > 100:
  print(f"Usted tiene {participantes} participantes en este evento, recuerde que el cupo maximo son 100 participantes")