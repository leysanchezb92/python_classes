#Crear una clase Producto con atributos privados para nombre y precio. Usa getters y setters para acceder y modificar estos atributos.

class Product():
    def __init__(self, name: str, price: float, units: int):
        """
        Initialize Product.

        Args:
            name (str): Product name (Ex: 'Laptop')
            price (float): Product price. (Ex: '10.50')
            units (int): Units available of the product. (Ex: '5')
        """
        self.__name = name
        self.__price = price
        self.units = units
        
    @property
    def name(self):
        """
        Returns a new name.
        """
        print("Access new name...")
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 3:
            print("New name active...")
            self.__name = new_name
        else:
            print(f"This name is incorrect, please verify the name: {new_name}")
    
    @property
    def price(self):
        print("Access new price...")
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print(f"Please add a valid price: {new_price}")
        else:
            print(f"This is the new price: {new_price}")
            self.__price = new_price