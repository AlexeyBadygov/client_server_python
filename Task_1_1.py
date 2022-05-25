"""
Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных
"""


def string_format_plus_type_chek(items):
    """
    Функция проверки типа и содержания переменных.
    :param items:
    :return:
    """
    for item in items:
        print(item)
        print(type(item))
    print(end='\n')


some_string_1 = 'разработка'
some_string_2 = 'сокет'
some_string_3 = 'декоратор'

some_list = [some_string_1, some_string_2, some_string_3]

string_format_plus_type_chek(some_list)

some_string_1_unicode = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
some_string_2_unicode = '\u0441\u043e\u043a\u0435\u0442'
some_string_3_unicode = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

some_list_unicode = [some_string_1_unicode, some_string_2_unicode, some_string_3_unicode]

string_format_plus_type_chek(some_list_unicode)
