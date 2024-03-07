from src.keyboard import Keyboard
import pytest


@pytest.fixture
def fixture():
    keyboard = Keyboard('клав_apple', 2000.00, 10)
    return keyboard

@pytest.fixture
def fixture_1():
    keyboard_1 = Keyboard('клав_xiaomi', 500.00, 1)
    return keyboard_1

keyboard_2 = Keyboard('клав_dns', 100.00, 100)


def test_name(fixture, fixture_1):
    """Проверка свойства name"""
    assert fixture.name == 'клав_apple'
    fixture.name = 'Кобылятников'
    assert fixture.name == 'Кобылятник'
    assert fixture_1.name == 'клав_xiaomi'
    assert fixture.language =="EN"


def test_repr(fixture, fixture_1):
    """Проверка функции представления"""
    assert fixture.__repr__() == "Keyboard('клав_apple', 2000.0, 10)"
    assert fixture_1.__repr__() == "Keyboard('клав_xiaomi', 500.0, 1)"


def test_str(fixture, fixture_1):
    """Проверка функции представления для пользователя"""
    assert fixture.__str__() == "клав_apple"
    assert fixture_1.__str__() == "клав_xiaomi"


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
    assert keyboard_2.apply_discount() == 100.00
    keyboard_2.pay_rate = 2.0
    assert keyboard_2.apply_discount() == 100.00
    assert fixture.apply_discount() == 2000.00
    assert fixture_1.apply_discount() == 500.00


def test_instantiate_from_csv(fixture, fixture_1):
    """Проверяем инициализацию экземплярами класса"""
    assert isinstance(fixture, Keyboard)
    assert isinstance(fixture_1, Keyboard)


def test_string_to_number():
    """статический метод, возвращающий число из числа-строки"""
    assert Keyboard.string_to_number('5') == 5
    assert Keyboard.string_to_number('5.0') == 5
    assert Keyboard.string_to_number('5.5') == 5

def test_change_lang():
    """метод, меняющий язык на клавиатуре"""
    assert keyboard_2.language == 'EN'
    keyboard_2.change_lang()
    assert keyboard_2.language == 'RU'




