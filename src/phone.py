from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float | int, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim
    
    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value > 0:
            self._number_of_sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other):
        if isinstance(self, Phone) and isinstance(other, Phone | Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя сложить 'Phone' или 'Item' с экземплярами классов не 'Phone' или 'Item'")

    def __radd__(self, other):
        if isinstance(self, Item) and isinstance(other, Phone | Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя сложить 'Phone' или 'Item' с экземплярами классов не 'Phone' или 'Item'")
