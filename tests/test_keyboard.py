import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard("keyboard", 5000, 6)


def test_init_keyboard(keyboard):
    assert keyboard.name == "keyboard"
    assert keyboard.price == 5000
    assert keyboard.quantity == 6


def test_language(keyboard):
    assert keyboard.language == 'EN'


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'
