# Solicita la cantidad de asistentes a una conferencia y calcula cuántos asientos quedan libres en un auditorio de 120 personas.

asistentes = int(input("Ingrese el numero de asistentes: "))
auditorio = 120
auditorio -= asistentes
print(f"Numero de asientos libres esl {auditorio}");