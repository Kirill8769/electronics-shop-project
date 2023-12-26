import pytest

from src.phone import Phone


@pytest.fixture
def init_class():
    return "iPhone 14", 120_000, 5, 2


def test_class_phone_init(init_class):
    result = Phone(*init_class)
    assert str(result) == 'iPhone 14'
    assert repr(result) == "Phone('iPhone 14', 120000, 5, 2)"
    assert result.number_of_sim == 2


def test_class_phone_add(init_class):
    result = Phone(*init_class)
    assert result + result == 10


def test_class_phone_raise():
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120_000, 5, 0)
