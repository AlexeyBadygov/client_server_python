"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных.
"""


def change_to_bytes_types(items):
    """
    Функция перевода записи в байтовый тип, без преобразованияи. Определение типа, содержимое и длину переменных.
    :param items:
    :return:
    """
    for item in items:
        el = eval(f"b'{item}'")
        print(f'{el}')
        print(f'Тип переменной: ', type(el))
        print(f'Длина переменной в байтах {len(item)}')
        print(end='\n')


some_string_1 = 'class'
some_string_2 = 'function'
some_string_3 = 'method'
some_list = [some_string_1, some_string_2, some_string_3]

change_to_bytes_types(some_list)
