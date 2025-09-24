# Crear una clase Calculadora con métodos estáticos para sumar, restar, multiplicar y dividir.

class Calculadora:
    def __init__(self, number1: float, number2: float):
        self.number1 = number1
        self.number2 = number2

    def suma(self):
        suma = self.number1 + self.number2
        return suma

    def resta(self):
        resta = self.number1 - self.number2
        return resta

    def multiplicar(self):
        multiplicar = self.number1 * self.number2
        return multiplicar

    def dividir(self):
        dividir = self.number1 / self.number2
        return dividir

mi_calculadora = Calculadora(10, 13)
print(f'Con los numeros entregados {mi_calculadora.number1} y {mi_calculadora.number2}, el resultado de la suma es: {mi_calculadora.suma()}, la resta es: {mi_calculadora.resta()}, la multiplicacion es: {mi_calculadora.multiplicar()} y la division es: {mi_calculadora.dividir()}')
