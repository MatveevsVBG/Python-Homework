"""
Задача 6: Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
"""
class NewEx(Exception):
    pass
try:
    num = int(input('Введите шестизначное число: '))
    if num > 999999 or num < 100000:
        raise NewEx()
except NewEx:
    print("Введён не шестизначный номер!")
else:
    res1 = 0
    count = 0
    while count < 3:
        tmp1 = num % 10
        res1 += tmp1
        num //= 10
        count += 1
    res2 = 0
    while num > 0:
        tmp2 = num % 10
        res2 += tmp2
        num //= 10
    if res1 == res2:
        print('Это счастливый билет!')
    else:
        print('Это обычный билет')