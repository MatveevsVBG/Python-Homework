"""
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
"""


def sum_two_numbers(x, y):
    if x == 0:
        return y
    return sum_two_numbers(x - 1, y + 1)


try:
    a, b = int(input("Ведите два целых неотрицательных числа:\n")), int(input())
    if a < 0 or b < 0:
        raise ValueError
except ValueError:
    print("Неверный ввод!")
else:
    print(sum_two_numbers(a, b))
