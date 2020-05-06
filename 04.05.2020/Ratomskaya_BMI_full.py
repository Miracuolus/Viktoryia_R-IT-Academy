from Person import *

def get_bmi(mass, height):
    """Возвращает индекс массы тела"""
    return mass/(height/100)**2


min_index = 16
max_index = 40


def print_scale(index):
    """Выводит индекс массы тела в виде шкалы"""
    index = max(min(round(index), max_index), min_index)
    left = index - min_index
    right = max_index - index
    print(str(min_index) + '=' * left + '|' + '=' * right + \
        str(max_index))

exit = ''
while exit.lower() != 'exit':
    family_name = input('Введите фамилию: ')
    name = input('Введите имя: ')
    father_name = input('Введите отчество: ')
    try:
        height = int((input('Введите рост в cм: ')))
        mass = float((input('Введите массу тела в кг: ')))
        age = int(input('Введите количество полных лет: '))
        person = Person(family_name, name, father_name, height, mass, age)
        print(person)
        body_index = get_bmi(mass, height)
        print(f'{person.get_name()}, Ваш индекс массы тела: {round(body_index, 2)}')
        print_scale(body_index)
    except ValueError:
        print('*Ошибка! В полях "Рост", "Вес", и "Возраст" необходимо'
            'вводить числовые значения')
    except InvalidHeight:
        print('*Ошибка! Введите реальное значение роста')
    except InvalidMass:
        print('*Ошибка! Введите реальное значение веса')
    except InvalidAge:
        print('*Ошибка! Введите реальное значение возраста')

    exit = input('Если хотите выйти из программы, то введите exit: ')


