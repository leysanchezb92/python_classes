# Crear una clase Calculadora con métodos estáticos para sumar, restar, multiplicar y dividir.

class Calculadora:
    def __init__(self, number1: float, number2: float):
        self.number1 = number1
        self.number2 = number2

    @staticmethod
    def suma(number1, number2):
        suma = number1 + number2
        return suma

    @staticmethod
    def resta(number1, number2):
        resta = number1 - number2
        return resta

    @staticmethod
    def multiplicar(number1, number2):
        multiplicar = number1 * number2
        return multiplicar

    @staticmethod
    def dividir(number1, number2):
        dividir = number1 / number2
        return dividir

mi_calculadora = Calculadora(10, 13)
print(f'Con los numeros entregados {mi_calculadora.number1} y {mi_calculadora.number2}, el resultado de la suma es: {Calculadora.suma(mi_calculadora.number1, mi_calculadora.number2)}, la resta es: {Calculadora.resta(mi_calculadora.number1, mi_calculadora.number2)}, la multiplicacion es: {Calculadora.multiplicar(mi_calculadora.number1, mi_calculadora.number2)} y la division es: {Calculadora.dividir(mi_calculadora.number1, mi_calculadora.number2)}')
