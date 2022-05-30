"""
Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку
созданного файла (исходить из того, что вам априори неизвестна кодировка этого файла!).
Затем открыть этот файл и вывести его содержимое на печать.
ВАЖНО: файл должен быть открыт без ошибок вне зависимости от того,
в какой кодировке он был создан!
"""
from chardet import detect

some_list = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as file:
    for word in some_list:
        file.write(f'{word}\n')
file.close()

# узнаем кодировку
with open('test_file.txt', 'rb') as file:
    content = file.read()
encoding = detect(content)['encoding']
print(encoding) #   windows-1251

# открываем в нужной кодеровке
with open('test_file.txt', 'r', encoding=encoding) as file:
    content = file.read()
print(content)
