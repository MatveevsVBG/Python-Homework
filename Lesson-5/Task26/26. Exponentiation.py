"""
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
"""


def exponent(x, y):
    if y == 0:
        return 1
    if y < 0:
        return 1 / exponent(x, -y)
    if y % 2 == 0:
        return exponent(x, y // 2) * exponent(x, y // 2)
    else:
        return exponent(x, y-1) * x


a = int(input("Введите число: "))
try:
    b = int(input("Введите степень числа: "))
except ValueError:
    print("Введено не целое число!")
else:
    print(f'{a} в степени {b} = {exponent(a, b)}')
