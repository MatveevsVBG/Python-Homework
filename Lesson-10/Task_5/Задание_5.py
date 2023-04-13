"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet с функцией detect для распознавания исходной
кодировки
"""


import subprocess
import chardet
import os

ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    # print(line.decode('utf-8'))  # для английской версии win10 работает, для русской?? нужен chardet.detect
    # print(chardet.detect(line))  # выводит словарь с кодировкой строк
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))  # из словаря берётся кодировка для декодирования

ARGS = ['ping', 'youtube.com']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))

print(os.name)



