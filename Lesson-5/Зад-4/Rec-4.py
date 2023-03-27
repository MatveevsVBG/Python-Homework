"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def sum_row_elem(n, elem=1, sum_elem=0):
    if n == 0:
        return sum_elem
    sum_elem = sum_elem + elem
    elem = elem * -0.5
    n -= 1
    return sum_row_elem(n, elem, sum_elem)


num = int(input('Кол-во элементов: '))
print(sum_row_elem(num))
