import csv
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = Item.pay_rate * self.price

    @property
    def name(self):
        """Геттер для приватного атрибута name.
        Возвращает значение приватного атрибута name."""
        return self.__name

    @name.setter
    def name(self, item):
        """Сеттер для приватного атрибута name.
        Присваивает значение приватному атрибуту name.
        Если длина переданного значения больше 10 символов, обрезает его до 10 символов."""
        if len(item) > 10:
            self.__name = item[:11]
        self.__name = item

    @classmethod
    def instantiate_from_csv(cls, file_path) -> None:
        """класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        cls.all.clear()
        file_path = Path(__file__).parent.joinpath("items.csv")
        with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            for item in data:
                name = item['name']
                price = cls.string_to_number(item['price'])
                quantity = int(item['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str) -> float:
        """статический метод, возвращающий число из числа-строки"""
        return int(float(value))

    def __add__(self, other) -> int:
        if isinstance(other, Item):
            return self.quantity + other.quantity
