# Pide el nombre de una empresa y el año de fundación, luego muestra cuántos años lleva en funcionamiento.

nombreEmpresa=input("Ingrese el nombre de la empresa: ");
anoFuncacion=int(input("Ingrese año de funcacion de la empresa: "));
anoActual=2025
anoActual -= anoFuncacion

print(f"La empresa se fundo hace {anoActual}")