import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone(name="IPhone", price=60000, quantity=5, number_of_sim=3)


def test_phone_init(phone):
    """Проверка наименования, цены и количества товара"""
    assert phone.name == "IPhone"
    assert phone.price == 60000
    assert phone.quantity == 5
    assert phone.number_of_sim == 3


def test_phone_repr(phone):
    assert repr(phone) == "Phone('IPhone', 60000, 5, 3)"


def test_phone_str(phone):
    assert str(phone) == 'IPhone'


def test_number_of_sim(phone):
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
