# Задача 2: Найдите сумму цифр трехзначного числа.

num = int(input('Введите трёхзначное число: '))
n = num
res = 0
while num > 0:
    tmp = num % 10
    res += tmp
    num //= 10
print(f'Сумма цифр числа {n} = {int(res)}')