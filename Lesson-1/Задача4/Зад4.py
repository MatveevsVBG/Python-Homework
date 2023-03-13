"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
если известно, что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
"""
# s = pet + ser + 2*(pet+ser) =>  s = 3pet + 3ser =>  s = 6pet

s = int(input("Введите количество журавликов кратное 6: "))
if s % 6 == 0:
    pet = s // 6
    kat = pet * 4
    print(f'Серёжа сделал {pet} журавликов, Петя - {pet}, Катя - {kat}')
else:
    print(f'Количество журавликов должно делиться на 6 без остатка!')