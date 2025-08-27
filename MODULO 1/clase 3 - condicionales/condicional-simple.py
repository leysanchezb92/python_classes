#ciclo - for - yo se la cantidad de veces que se va a repetir
#bucle - while - cuando yo no se cuantas veces se va a repetir
# monto total de retiros y transacciones, agregar usuario y contraseña, si coloco la contraseña mal 3 veces me saque de la aplicacion.

saldo = 5.000
historialRetiros = []
historialDepositos = []
clave = "1234"
usuario = "mojito"
contador = 1
intentos = 3

while True:
  usuarioIngreso = input("Ingrese su usuario: ")
  claveIngreso = input("Ingrese su contraseña: ")
  if usuario == usuarioIngreso and clave == claveIngreso and contador < 3:
    contador = 1
    print("\n ----MENU----")
    print("1. Ver Saldo")
    print("2. Retirar Dinero")
    print("3. Depositar Dinero")
    print("4. Ver historial de movimientos")
    print("5. Cambiar clave")
    print("6. Monto total de retiros")
    print("7. Monto total de consignaciones")
    print("8. Salir")
    
    opcion = int(input("Digite la opcion: "))
    
    if opcion == 1:
        print(f"su saldo actual es: {saldo:.3f}")
    elif opcion == 2:
        monto = float(input("cuanto deseas retirar? "))
        if monto <= saldo:
            saldo -= monto
            historialRetiros.append(monto)
            print(historialRetiros)
            print(f"Retiraste {monto:.3f}")
            print(f"Retiro exitoso. Saldo restante ${saldo:.3f}")
        else:
            print("Saldo insuficiente")            
    elif opcion == 3:
        monto = float(input("Cuanto quieres depositar? "))
        if monto > 0:
            saldo += monto 
            historialDepositos.append(monto)
            print(historialDepositos)
            print(f"Depositaste {monto:.3f}")
            print(f"Deposito exitoso el nuevo saldo es: {saldo:.3f}")
        else:
            print("No puedes depositar montos negativos")            
    elif opcion == 4:
        print("historialRetiros")
        if len(historialRetiros) == 0:
            print("No tienes movimientos")
        else:
            for movimiento in historialRetiros:
                print(movimiento)   
    elif opcion == 5:
        intento = input("Escribe tu clave actual: ")
        if intento == clave:
            nueva = input("Digita tu nueva clave: ")
            clave = nueva 
            print("Tu clave a sido cambiada con exito ")            
        else:
            print("Clave incorrecta. ")
    elif opcion == 6:
      monto = 0
      for retiro in historialRetiros:
        monto += retiro
      print(f"Usted ha retirado un total de ${monto:.3f}")
    elif opcion == 7:
      monto = 0
      for consignacion in historialDepositos:
        monto += consignacion
      print(f"Usted ha consignado un total de ${monto:.3f}")
    elif opcion == 8:
        print("gracias por usar nuestro sistema: ")
        break
    else:
        print("Opcion invalida")
  elif contador >= 3:
    print(f"Ha superado el numero de intentos validos {contador}, intente nuevamente en 2 mins")
    break
  elif usuario != usuarioIngreso or clave != claveIngreso:
    print(f"Usuario o contraseña invalida, intente nuevamente, usted cuenta con {intentos - contador} intentos más")
    contador += 1
  
