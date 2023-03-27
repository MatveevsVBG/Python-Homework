"""
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
"""


def reverse_number(num_1, num_2=0):
    if num_1 == 0:
        return num_2
    n = num_1 % 10
    num_2 = num_2 * 10 + n
    num_1 = num_1 // 10
    return reverse_number(num_1, num_2)


number = int(input("Введите число: "))
print(reverse_number(number))
