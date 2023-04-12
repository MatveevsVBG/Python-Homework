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

byte_lists = [bytes(word, 'utf-8') for word in words]

for i, byte_list in enumerate(byte_lists):
    print(f"Слово {words[i]}:")
    print(f"\tТип: {type(byte_list)}")
    print(f"\tСодержимое: {byte_list}")
    print(f"\tДлина: {len(byte_list)}")
