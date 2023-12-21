import pytest

from src.item import Item


@pytest.fixture()
def init_data():
    return "Смартфон", 10000, 20


def test_class_item_init(init_data):
    result = Item(*init_data)
    assert result.calculate_total_price() == 200000
    Item.pay_rate = 0.8
    result.apply_discount()
    assert result.price == 8000.0
    assert isinstance(result, Item) is True


@pytest.mark.parametrize("name, price, quantity", [
    (123, 10000, 20),
    ("Смартфон", "incorrect", 20),
    ("Смартфон", 10000, "incorrect")
])
def test_class_item_incorrect_type(name, price, quantity):
    with pytest.raises(TypeError):
        Item(name, price, quantity)
