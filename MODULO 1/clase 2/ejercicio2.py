# Pide el salario base de un empleado y calcula su salario total con un bono del 15%.
salario=int(input("Ingrese el salario base: "))
totalSalario= salario + (salario*0.15)

print(f"El salario mas bono es {totalSalario}")