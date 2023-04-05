# Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными.
# Для этого:
#  - Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
# orders.json. При записи данных указать величину отступа в 4 пробельных символа;
#  - Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import os
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def write_order_to_json(item, quantity, price, buyer, date):
    filename = os.path.join(CURRENT_DIR, 'orders.json')

    with open(filename, encoding="utf-8") as my_f:
        data = json.loads(my_f.read())

    data['orders'].append({'item': item, 'quantity': quantity, 'price': price,
                           'buyer': buyer, 'date': date})

    with open(filename, "w", encoding="utf-8") as my_f:
        json.dump(data, my_f, indent=4, separators=(',', ': '), ensure_ascii=False)
    print(f'Данные добавлены в {filename}')


write_order_to_json('Марк Лутц - Изучаем Python', '10',
                    '300', 'Иванов', '03.04.2023')
write_order_to_json('Майкл Доусон - Программируем на Python', '15',
                    '400', 'Петров', '04.04.2023')
write_order_to_json('Дэн Бейдер - Чистый Python. Тонкости программирования для профи',
                    '20', '500', 'Сидоров', '05.04.2023')