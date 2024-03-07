import csv
import os


class InstantiateCSVError(Exception):
    print("Файл item.csv поврежден")


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise Exception


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_price_product = self.price * self.quantity * Item.pay_rate
        return total_price_product


    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price


    @classmethod
    def instantiate_from_csv(cls):
        """класс - метод, инициализирующий экземпляры класса `Item` данными из файла
        _src / items.csv_"""
        docs = os.path.abspath('../src/items.csv')
        try:
            with open(docs, 'r') as csvfile:
                fieldnames = ['name', 'price', 'quantity']
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                for row in reader:
                    if row['price'] == "" or row['name'] == "" or row['quantity'] == "":
                        cls(row['name'], row['price'], row['quantity'])
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            print('Отсутствует файл item.csv')



    def string_to_number(text):
        """статический метод, возвращающий число из числа-строки"""
        if text.isdigit():
            return int(text)
        elif float(text):
            text_int = int(float(text))
            return text_int

