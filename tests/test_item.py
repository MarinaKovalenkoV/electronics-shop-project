"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


item1 = Item('помидор', 2000.20, 10)
item2 = "10"
item3 = "10.1"

def test_calculate_total_price():
    """Когда мы передаем сумму товара и кол-во, то функция перемножит сумму на кол-во"""
    assert Item.calculate_total_price(item1) == 20002.0


def test_apply_discount():
    """Когда мы передаем сумму товара, то функция перемножит сумму на скидку"""
    pay_rate = 0.8
    assert Item.apply_discount(item1) == 2000.2


#def test_instantiate_from_csv():
    #assert pass


def test_string_to_number():
    assert Item.string_to_number(item2) == 10
    assert Item.string_to_number(item3) == 10