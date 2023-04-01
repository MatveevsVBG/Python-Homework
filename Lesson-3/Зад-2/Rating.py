"""
2. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

rating = [7, 6, 5, 4, 3, 3, 2, 1]
new_elem = int(input("Введите новый элемент рейтинга: "))
print(rating)
max_value = max(rating)
if new_elem > max_value:
    rating.insert(0, new_elem)
elif new_elem in rating:
    rating.insert((rating.index(new_elem) + 1), new_elem)
else:
    rating.append(new_elem)
print(rating)
