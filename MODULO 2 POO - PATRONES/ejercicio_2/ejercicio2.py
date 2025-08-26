# Crear una clase CuentaBancaria con atributos para titular y saldo. Debe tener métodos para depositar y retirar dinero.

class CuentaBancaria():
    def __init__(self, titular: str, saldo: float = 0.0):
        """
		Inicializa Cuenta Bancaria.

		Args:
			titular (str): Nombre persona dueña de cuenta. (Ej: 'Pedro')
			Saldo (str): Dinero en cuenta. (Ej: '10.000')
		"""
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad: float):
        """
        Deposita una cantidad de dinero en la cuenta.
        """
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de ${cantidad:,.2f} realizado.")
            self.mostrar_saldo()
        else:
            print('la cantidad a depositar debe ser positiva')
    
    def retirar(self, cantidad: float):
        """
		Método para imprimir la cantidad a retirar segun su saldo
        """
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad:,.2f} realizado.")
            self.mostrar_saldo()
        else:
            print('Fondos insufientes')
    
    def mostrar_saldo(self):
        """
		Método para imprimir el saldo del titular
        """
        print(f'Saldo actual de {self.titular}: ${self.saldo:,.2f}')
        
