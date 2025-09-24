class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self._speed = 0

    def fuel_consumption(self):
        pass

class Auto(Vehicle):
    def __init__(self, brand, model, fuel):
        super().__init__(brand, model)
        self.fuel = 100

    def fuel_consumption(self):
        distance = 0

        if distance == 10:
            self.fuel -= 2
            distance += 1
        else:
            distance +=1
        #Implementa el método consumir_combustible(): su lógica debe ser que por cada 10 km que se desplaza, consume 2 unidades de combustible.