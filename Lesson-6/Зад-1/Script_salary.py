"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


from sys import argv

script_name, prod_in_ours, rare_per_hour, bonus = argv

salary = int(prod_in_ours) * int(rare_per_hour) + int(bonus)
print("Имя скрипта: ", script_name)
print("Выработка в часах: ", prod_in_ours)
print("Ставка в час: ", rare_per_hour)
print("Премия: ", bonus)
print("Заработная плата сотрудника: ", salary, '$')
