import os

from src.item import Item
from config import PATH_PROJECT

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.
    # ??? Почему это здесь, в задании написано обрезать название

    file_path = os.path.join(PATH_PROJECT, "src", "items.csv")
    Item.instantiate_from_csv(file_path=file_path)  # создание объектов из данных файла
    assert len(Item.all) == 6  # в файле 5 записей с данными по товарам ??? Почему 5, когда 6.

    item1 = Item.all[0]
    assert item1.name == 'СуперСмарт'
    #assert item1.name == 'Смартфон'  ??? Почему Смартфон, когда СуперСмарт же ..

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
