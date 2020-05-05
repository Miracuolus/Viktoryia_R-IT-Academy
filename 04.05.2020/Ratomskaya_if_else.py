try:
    value_1 = int(input('Введите первое значение: '))
    value_2 = int(input('Введите второе значение: '))
    value_3 = int(input('Введите третье значение: '))
except ValueError:
    print('*Ошибка! Введите целое число.')

((value_1 and value_2 and value_3) or print('1) -')) and\
    print('1) Нет нулевых значений')


(value_1 == 0 or print(f'2) {value_1}')) and (value_2 == 0 or\
    print(f'2) {value_2}')) and (value_3 == 0 or\
        print(f'2) {value_3}')) and print('2) Введены все нули')

if value_1 > (value_2 + value_3):
    print(f'3) {value_1 - value_2 - value_3}')
else:
    print('3) -')

if value_1 < (value_2 + value_3):
    print(f'4) {value_2 + value_3 - value_1}')
else:
    print('4) -')

if value_1 > 50 and (value_2 > value_1 or value_3 > value_1):
    print('5) Вася')
else:
    print('5) -')

if value_1 > 5 or (value_2 == 7 and value_3 == 7):
    print('6) Петя')
else:
    print('6) -')