"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
"""

seasons = ["зима", "весна", "лето", "осень"]
try:
    month = int(input("Введите номер месяца: "))
    if month < 1 or month > 12:
        raise ValueError
except ValueError:
    print("Введены неверные даннные!")
else:
    if month in (1, 2, 12):
        print(seasons[0])
    elif month in (3, 4, 5):
        print(seasons[1])
    elif month in (6, 7, 8):
        print(seasons[2])
    else:
        print(seasons[3])


# seasons = {0: "зима", 1: "весна", 2: "лето", 3: "осень"}
# try:
#     month = int(input("Введите номер месяца: "))
#     if month < 1 or month > 12:
#         raise ValueError
# except ValueError:
#     print("Введены неверные даннные!")
# else:
#     if month in (1, 2, 12):
#         print(seasons[0])
#     elif month in (3, 4, 5):
#         print(seasons[1])
#     elif month in (6, 7, 8):
#         print(seasons[2])
#     else:
#         print(seasons[3])
