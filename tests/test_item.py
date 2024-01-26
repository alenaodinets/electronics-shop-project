"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item(name="supercomputer", price=50000, quantity=5)


def test_item_init(item):
    """Проверка наименования, цены и количества товара"""
    assert item.name == "supercomputer"
    assert item.price == 50000
    assert item.quantity == 5


def test_calculate_total_price(item):
    """Проверка подсчета общем стоимости конкретного товара"""
    assert item.calculate_total_price() == 250000


def test_apply_discount(item):
    """Проверка новой цены с учетом скидки"""
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 40000


def test_string_to_number(item):
    """Проверка на перевед с str в int"""
    assert item.string_to_number('5') == 5
    assert item.string_to_number('5.0') == 5
    assert item.string_to_number('5.5') == 5
