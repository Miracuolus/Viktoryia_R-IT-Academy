from Person import *
class InvalidName(Exception):
    """Класс вызова исключения при некорректном ФИО"""
    pass

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

def recomendation(person):
    """Рекомендации по результатам расчета ИМТ"""
    body_index = get_bmi(person.get_mass(), person.get_height()) 
    if (body_index < 16) and (person.get_age() >= 13):
        print(f'{person.get_name()}, у Вас выраженный дефицит массы тела')
        print('Вам следует обратиться к врачу.')
    elif (16 <= body_index <= 18.49):
        print(f'{person.get_name()}, у Вас недостаточная масса тела')
        print('Для нормализации веса важен полноценный отдых, правильное '
        'питание, умеренная физическую активность.')
    elif (18.5 <= body_index <= 24.99) and (19 <= person.get_age() <= 24):
        print(f'{person.get_name()}, у Вас нормальный вес')
        print('Рекомендации вам не требуются.')
    elif 25 <= body_index <= 29.99:
        print(f'{person.get_name()}, у Вас предожирение')
        print('Вам следует отказаться от избыточного потребления пищи,\n'
        'заняться физической акттивностью, следить за своим '
        'психоэмоциональным состоянием.')
    elif body_index >= 30:
        if 30 <= body_index <= 34.99:
            print(f'{person.get_name()}, у Вас ожирение 1-ой степени')
        elif 35 <= body_index <= 39.99:
            print(f'{person.get_name()}, у Вас ожирение 2-ой степени')
        elif body_index >= 40:
            print(f'{person.get_name()}, у Вас ожирение 3-ой степени')
        print('Вам следует обратиться к врачу, который подберет вам '
        'методику решения проблемы с ожирением.')
    else:
        print(f'{person.get_name()}, у Вас нормальный вес')
        print('Рекомендации вам не требуются.')

def check_names(name):
    """Функция для определения валидности полей ФИО"""
    if name == '' or name == ' '*len(name):
        raise InvalidName
        
people = []
exit = ''
while exit.lower() != 'exit':
    try:
        family_name = input('Введите фамилию: ')
        check_names(family_name) # проверка на валидность поля
        name = input('Введите имя: ')
        check_names(name) # проверка на валидность поля
        father_name = input('Введите отчество: ')
        check_names(father_name) # проверка на валидность поля
        height = int((input('Введите рост в cм: ')))
        mass = float((input('Введите массу тела в кг: ')))
        age = int(input('Введите количество полных лет: '))
        person = Person(family_name, name, father_name, height, mass, age)
        print(person)
        body_index = get_bmi(person.get_mass(), person.get_height()) # расчет индекса массы тела
        print(f'{person.get_name()}, Ваш индекс массы тела: {round(body_index, 2)}')
        print_scale(body_index) # вывод шкалы
        recomendation(person)
    except ValueError:
        print('*Ошибка! В полях "Рост", "Вес", и "Возраст" необходимо'
            'вводить числовые значения')
    except InvalidName:
        print('*Ошибка! Поле ФИО не должно быть пустым или содержать пробелы')
    except InvalidHeight:
        print(f'*Ошибка! Некорректное значение роста: {height}')
    except InvalidMass:
        print(f'*Ошибка! Некорректное значение веса: {mass}')
    except InvalidAge:
        print(f'*Ошибка! Некорректное значение возраста: {age}')
    
    people.append(person) # если все поля валидные, то добавляем пользователя в список
    exit = input('Если хотите выйти из программы, то введите exit: ')



