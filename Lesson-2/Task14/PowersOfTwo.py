"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.
"""
num = int(input("Введите число N: "))
temp = 1
while temp < num:
    print(temp, end=" ")
    temp *= 2


# i = 0
# while 2 ** i <= num:
#     print(2 ** i)
#     i += 1
