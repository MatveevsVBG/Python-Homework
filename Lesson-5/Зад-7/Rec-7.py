"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
"""


def proof_equality(n, sum1=0):
    if n == 0:
        return sum1
    sum1 = sum1 + n
    n -= 1
    return proof_equality(n, sum1)


num = int(input('n='))
x = proof_equality(num)
if x == num * (num + 1) / 2:
    print('Равенство верно')
else:
    print('Равенство не верно')


