"""
Задание 2.
Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


words = ['class', 'function', 'method']

for word in words:
    byte_word = bytes(word, "ascii")
    print(f'Переменная {word}:')
    print(f"\tТип: {type(byte_word)}")
    print(f"\tСодержимое: {byte_word}")
    print(f"\tДлина: {len(byte_word)}")
