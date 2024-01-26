"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item(name="computer", price= 50000, quantity=5)

def test_item_init(item):
    """Проверка наименования, цены и количества товара"""
    assert item.name == "computer"
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