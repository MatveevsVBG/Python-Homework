"""
3. Реализовать структуру данных «Товары». Она должна представлять собой
список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.
"""

products, order = [], 1
title, price, amount = None, None, None
while True:
    if title is None:
        title = input('Введите название товара: ')

    if price is None:
        price = int(input('Введите стоимость товара: '))

    if amount is None:
        amount = int(input('Введите количество: '))

    unit = input('Введите единицы измерения: ')

    products.append((order,
                     {'название': title, 'цена': price, 'кол-во': amount,
                      'ед': unit}))
    title, price, amount = None, None, None
    order += 1
    print(products)

    q = input('Формирование списка завершено? (y/N)) ')
    if q.lower() == 'y':
        break

analitics = {'название': [], 'цена': [], 'кол-во': [], 'ед': set()}
for _, item in products:
    analitics['название'].append(item['название'])
    analitics['цена'].append(item['цена'])
    analitics['кол-во'].append(item['кол-во'])
    analitics['ед'].add(item['ед'])

print(analitics)
