import os
from src.item import Item

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    file = os.path.abspath(r'C:\Users\manto\PycharmProjects\electronics-shop-project/src/items.csv')
    Item.instantiate_from_csv(file)  # создание объектов из данных файла
    assert (len(Item.all) == 5)  # в файле 5 записей с данными по товарам
    print(Item.all[0])

    item1 = Item.all[0]
    print(item1)
    #print(item1.name)
    print(item1['name'])
    #assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
