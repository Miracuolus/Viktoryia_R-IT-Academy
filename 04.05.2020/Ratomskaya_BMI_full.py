from Person import *
class InvalidName(Exception):
    """Класс вызова исключения при некорректном ФИО"""
    pass

class InvalidAction(Exception):
    """Класс вызова исключения при вводе в поле Выбор действия всех 
    чисел, кроме 1, 2, 3, 4"""
    pass

def create_names(second_name, name, father_name):
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
    cut_name = name.lstrip()
    #if name == '' or name == ' '*len(name):
    if cut_name == '':
        raise InvalidName

def check_action(action):
    if action <= 0 or action >= 5:
        raise InvalidAction
        
persons = []
exit = ''
while exit.lower() != 'exit':
    try:
        choose_action = int(input('Выберете действие:\n'
        '1 - создание нового пользователя,\n'
        '2 - вывод списка пользователей,\n'
        '3 - редактирование пользователя,\n'
        '4 - удаление пользователя.\n'))
        check_action(choose_action)
        if choose_action == 1:
            family_name = input('Введите фамилию: ')
            check_names(family_name)
            name = input('Введите имя: ')
            check_names(name)
            father_name = input('Введите отчество: ')
            check_names(father_name)
            height = int((input('Введите рост в cм: ')))
            mass = float((input('Введите массу тела в кг: ')))
            age = int(input('Введите количество полных лет: '))
            person = Person(family_name, name, father_name, height, mass, age)
            print(person)
            body_index = get_bmi(person.get_mass(), person.get_height())
            print(f'{person.get_name()}, Ваш индекс массы тела: {round(body_index, 2)}')
            print_scale(body_index)
            recomendation(person)
        elif choose_action == 2:
            for people in range(0, len(persons)):
                print(f'{people + 1}. '
                    f'{persons[people].get_second_name()} '
                    f'{persons[people].get_name()} '
                    f'{persons[people].get_father_name()}: '
                    f'рост - {persons[people].get_height()}, '
                    f'вес - {persons[people].get_mass()}, '
                    f'возраст - {persons[people].get_age()}')
        elif choose_action == 3:
            
    except ValueError:
        print('*Ошибка! В полях "Выбор действия", "Рост", "Вес", и '
            '"Возраст" необходимо вводить числовые значения')
    except InvalidAction:
        print('*Ошибка! В поле Выбора действия необходимо вводить число от 1 до 4 включительно')
    except InvalidName:
        print('*Ошибка! Поле ФИО не должно быть пустым или содержать пробелы')
    except InvalidHeight:
        print(f'*Ошибка! Некорректное значение роста: {height}')
    except InvalidMass:
        print(f'*Ошибка! Некорректное значение веса: {mass}')
    except InvalidAge:
        print(f'*Ошибка! Некорректное значение возраста: {age}')
    else: 
        if (len(persons) == 0) and (choose_action == 2):
            print('Не создано еще ни одного пользователя')
        else:
            persons.append(person)
    exit = input('Если хотите выйти из программы, то введите exit: ')