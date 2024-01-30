"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

class Test():
    @pytest.fixture
    def test(self):
        item1 = Item('помидор', 2000.20, 10)
        item2 = Item('сахар', 10.00, 0)
        item3 = Item('помидор', 00.00, 123)
        return item1, item2, item3

    item1 = ('../electronics-shop-project/src/items.csv')

    def test_calculate_total_price(self):
        """Когда мы передаем сумму товара и кол-во, то функция перемножит сумму на кол-во"""
        assert Item.calculate_total_price(item1) == 20000
        assert Item.calculate_total_price(item2) == 20000
        assert Item.calculate_total_price(item3) == 20000

    def test_apply_discount(self):
        """Когда мы передаем сумму товара, то функция перемножит сумму на скидку"""
        pay_rate = 0.8
        assert Item.apply_discount(test) * pay_rate == 1600.0

    def test_instantiate_from_csv(self):
        assert Item.instantiate_from_csv(item1) == 0
