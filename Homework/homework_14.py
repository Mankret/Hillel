# Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
# Декодировать её в строковый вид в кодировке по умолчанию.
# Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’.
# И на конец результат снова декодировать в строку. (результаты всех преобразований выводить на экран).

byte_str = b'r\xc3\xa9sum\xc3\xa9'
print("Before: ", byte_str)
decode_str = byte_str.decode()
print("After: ", decode_str)
print('-' * 30)
decode_str = decode_str.encode('Latin1')
print('Before: ', decode_str)
decode_str = decode_str.decode('Latin1')
print('After: ', decode_str)
