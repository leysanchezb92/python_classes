# Pide el número de horas trabajadas y la tarifa por hora, luego calcula el salario total.

horasTrabajadas= int(input("Ingrese el numero de horas trabajadas: "))
tarifaHora= float(input("Ingrese la trifa por hora: "))
totalPagar= horasTrabajadas * tarifaHora

print(f"El salario de este mes sera de {totalPagar} USD")