"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode)
"""

word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'

some_str = [word_1, word_2, word_3, word_4]
result_bytes = []
result_str = []
print(some_str)
print(end='\n')

for el in some_str:
    bytes_encoded = el.encode('utf-8')
    result_bytes.append(bytes_encoded)
    str_decoded = bytes_encoded.decode('utf-8')
    result_str.append(str_decoded)
    print(f'Encoded bytes = {bytes_encoded}')
print(end='\n')
print(f'Decoded string = {result_str}')
