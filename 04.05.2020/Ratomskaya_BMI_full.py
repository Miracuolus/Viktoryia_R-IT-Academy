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

def recomendation(index):
    """Рекомендации по результатам расчета ИМТ"""
    if index < 16:
        print(f'{person.get_name()}, у Вас выраженный дефицит массы тела')
    elif 16 <= body_index <= 18.49:
        print(f'{person.get_name()}, у Вас недостаточная масса тела')
    elif 18.5 <= body_index <= 24.99:
        print(f'{person.get_name()}, у Вас нормальный вес')
    elif 25 <= body_index <= 29.99:
        print(f'{person.get_name()}, у Вас предожирение')
    elif 30 <= body_index <= 34.99:
        print(f'{person.get_name()}, у Вас ожирение 1-ой степени')
    elif 35 <= body_index <= 39.99:
        print(f'{person.get_name()}, у Вас ожирение 2-ой степени')
    elif body_index >= 40:
        print(f'{person.get_name()}, у Вас ожирение 3-ой степени')
    else:
        print(f'{person.get_name()}, у Вас нормальный вес')

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
        recomendation(body_index)
    except ValueError:
        print('*Ошибка! В полях "Рост", "Вес", и "Возраст" необходимо'
            'вводить числовые значения')
    except InvalidHeight:
        print(f'*Ошибка! Некорректное значение роста: {height}')
    except InvalidMass:
        print(f'*Ошибка! Некорректное значение веса: {mass}')
    except InvalidAge:
        print(f'*Ошибка! Некорректное значение возраста: {age}')

    exit = input('Если хотите выйти из программы, то введите exit: ')


