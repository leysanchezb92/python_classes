# Solicita el presupuesto anual de una organización y calcula cuánto puede gastar mensualmente.

presupuestoAnual = int(input("Ingrese el presupuesto anual de su organización: "));
gastoPorMes = presupuestoAnual/12;

print(f"Usted puede tener un gasto mensual de {gastoPorMes} durante el año, de acuerdo con el presupuesto inicial de {presupuestoAnual}");