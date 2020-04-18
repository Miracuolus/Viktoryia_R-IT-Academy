#____________________Основная часть____________________
main_string = 'Не знаю, как там в Лондоне, я не была. Может, там собак\
а — друг человека. А у нас управдом — друг человека!'
print(f'Исходная строка: {main_string}')
print(f'Количество символов - {len(main_string)}')
print(f'Инверсная строка: {main_string[::-1]}')
print(f'Все слова с большой буквы: {main_string.title()}')
print(f'Весь текст прописными буквами: {main_string.upper()}')
print('Число вхождений "нд" = {0}, "ам" = {1}, "o" = {2}'
      .format(main_string.count('нд'), main_string.count('ам'),
              main_string.count('о')))
#____________________Собственные упражнения____________________
print('Строка заканчивается на "!" - {}'
      .format(main_string.endswith('!')))
print('Индекс первого упоминание элемента "a" = {}'
      .format(main_string.find('а')))
print('Индекс первого упоминание подстроки "друг" начиная с 70 элемент\
а исходной строки = {}'.format(main_string.index('друг', 70)))
print(f'Все символы в строке строчные? - {main_string.islower()}')
print('Каждый символ строки разделен пробелом: {}'
      .format(' '.join(main_string)))
dictionary = str.maketrans({'Л': 'L', 'д': 'd'})
print('Замена символов "Л" на "L", "д" на "d": {}'
      .format(main_string.translate(dictionary)))
print('Замена слова "друг" на "friend": {}'
      .format(main_string.replace('друг', 'friend')))
print('Замена строчных букв на прописные и наоборот: {}'
      .format(main_string.swapcase()))
print(f'Все символы в строке строчные: {main_string.lower()}')
