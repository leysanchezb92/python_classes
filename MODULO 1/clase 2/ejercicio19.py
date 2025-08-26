# Solicita el nombre de una ciudad y la temperatura actual, luego muestra si hace frío (≤18°C), calor (≥30°C) o clima templado.

ciudad = input("Ingrese el nombre de la ciudad: ");
temperatura = float(input("Ingrese la temperatura actual de la ciudad escogida previamente: "))

if temperatura <= 18:
  print(f"La temperatura de {ciudad} es de {temperatura}, y tenemos clima frio")
elif temperatura > 18:
  print(f"La temperatura de {ciudad} es de {temperatura}, y tenemos clima templado")
elif temperatura >= 30:
  print(f"La temperatura de {ciudad} es de {temperatura}, y hace calor")
  