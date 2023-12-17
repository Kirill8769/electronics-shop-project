import os
import csv
import re


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float | int, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = self.name = name
        if not isinstance(price, float | int):
            raise TypeError("В аргументе price ожидается тип данных float или int")
        self.price = price
        if not isinstance(quantity, int):
            raise TypeError("В аргументе quantity ожидается тип данных int")
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("В аргументе name ожидается тип данных str")
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, file_path: str):
        if not os.path.isfile(file_path):
            raise FileExistsError("Файл не найден")
        with open(file_path, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls(row["name"], float(row["price"]), int(row["quantity"]))

    @staticmethod
    def string_to_number(str_digit: str):
        if re.search(r"^\d[\d.]*$", str_digit):
            return int(float(str_digit))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
