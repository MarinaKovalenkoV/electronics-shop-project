"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone
import pytest

@pytest.fixture
def fixture():
    item = Item('помидор', 2000.00, 10)
    return item

@pytest.fixture
def fixture_1():
    item1 = Item('телефон', 500.00, 1)
    return item1

item2 = Item('скотч', 100.00, 100)

def test_name(fixture, fixture_1):
    """Проверка свойства name"""
    assert fixture.name == 'помидор'
    fixture.name = 'Кобылятников'
    assert fixture.name == 'Кобылятник'
    assert fixture_1.name == 'телефон'


def test_repr(fixture, fixture_1):
    """Проверка функции представления"""
    assert fixture.__repr__() == "Item('помидор', 2000.0, 10)"
    assert fixture_1.__repr__() == "Item('телефон', 500.0, 1)"


def test_str(fixture, fixture_1):
    """Проверка функции представления для пользователя"""
    assert fixture.__str__() == "помидор"
    assert fixture_1.__str__() == "телефон"


def test_add(fixture, fixture_1):
    """Проверка функции представления"""
    assert fixture.__add__(fixture_1) == 11
    assert fixture_1.__add__(fixture) == 11


def test_calculate_total_price(fixture, fixture_1):
    """Когда мы передаем сумму товара и кол-во, то функция перемножит сумму на кол-во"""
    assert fixture.calculate_total_price() == 20000.0
    assert fixture_1.calculate_total_price() == 500.0


def test_apply_discount(fixture, fixture_1):
    """Когда мы передаем сумму товара, то функция перемножит сумму на скидку"""
    assert item2.apply_discount() == 100.00
    item2.pay_rate = 2.0
    assert item2.apply_discount() == 100.00
    assert fixture.apply_discount() == 2000.00
    assert fixture_1.apply_discount() == 500.00


def test_instantiate_from_csv(fixture, fixture_1):
    """Проверяем инициализацию экземплярами класса"""
    assert isinstance(fixture, Item)
    assert isinstance(fixture_1, Item)


def test_string_to_number():
    """статический метод, возвращающий число из числа-строки"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
