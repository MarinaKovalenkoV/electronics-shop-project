import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone('nokia', 505.0, 1, 2)


def test_init(phone):
    assert phone.number_of_sim == 2
    assert phone.name == 'nokia'
    assert phone.price == 505.0
    assert phone.quantity == 1


def test_repr(phone):
    assert Phone.__repr__(phone) == "Phone('nokia', 505.0, 1, 2)"


def test_number_of_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = -1
        phone.number_of_sim = 0
