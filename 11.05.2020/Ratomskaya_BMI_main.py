from Person import *


class InvalidName(Exception):
    """Класс вызова исключения при некорректном ФИО"""
    pass


class InvalidAction(Exception):
    """ Класс вызова исключения при вводе в поле Выбор действия всех 
        чисел, кроме 0, 1, 2, 3, 4, 5 """
    pass


class InvalidNumberPerson(Exception):
    """ Класс вызова исключения при вводе несуществующего номера 
        пользователя"""
    pass


def check_action(action):
    if action < 0 or action > 5:
        raise InvalidAction


def check_names(name):
    """Функция для определения валидности полей ФИО"""
    cut_name = name.lstrip()
    if cut_name == '':
        raise InvalidName


def create_names():
    """Функция ввода ФИО"""
    family_name = input('Введите фамилию: ')
    check_names(family_name)
    name = input('Введите имя: ')
    check_names(name)
    father_name = input('Введите отчество: ')
    check_names(father_name)
    return (father_name, name, father_name)


def create_params():
    """Функция ввода параметров пользователя"""
    height = int((input('Введите рост в cм: ')))
    mass = float((input('Введите массу тела в кг: ')))
    age = int(input('Введите количество полных лет: '))
    create_params.height = height
    create_params.mass = mass
    create_params.age = age
    return(height, mass, age)


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
    print(str(min_index) + '=' * left + '|' + '=' * right +
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
              'питание, умеренная физическая активность.')
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


def choose_person():
    number = int(input(f'Введите номер пользователя (начиная с 1 до '
                       f'{len(persons)}): '))
    if 1 <= number <= len(persons):
        return number
    else:
        raise InvalidNumberPerson

def choose_action():
    choose_action = int(input('\nВыберете действие:\n'
                                  '0 - выход из программы\n'
                                  '1 - создание нового пользователя,\n'
                                  '2 - вывод списка пользователей,\n'
                                  '3 - редактирование пользователя,\n'
                                  '4 - удаление пользователя,\n'
                                  '5 - перерасчет ИМТ.\n'))
    check_action(choose_action)
    return choose_action

persons = []

def create_person():
    names = create_names()
    params = create_params()
    person = Person(*names, *params)
    persons.append(person)
    print(person)
    body_index = get_bmi(person.get_mass(), person.get_height())
    print(f'{person.get_name()}, Ваш индекс массы тела: '
        f'{round(body_index, 2)}')
    print_scale(body_index)
    recomendation(person)
    
 # Основная часть

while True:
    try:
        action = choose_action()
        if action == 0:
            break
        if action == 1:
            create_person()
        elif action == 2:
            if len(persons) == 0:
                print('Не создано еще ни одного пользователя')
            else:
                for people in range(0, len(persons)):
                    print(f'{people + 1}. '
                          f'{persons[people].get_second_name()} '
                          f'{persons[people].get_name()} '
                          f'{persons[people].get_father_name()}: '
                          f'рост - {persons[people].get_height()}, '
                          f'вес - {persons[people].get_mass()}, '
                          f'возраст - {persons[people].get_age()}')
        elif action == 3:
            if len(persons) == 0:
                print('Не создано еще ни одного пользователя')
            else:
                number_person = choose_person()
                update_params = create_params()
                persons[number_person-1].set_height(update_params[0])
                persons[number_person-1].set_mass(update_params[1])
                persons[number_person-1].set_age(update_params[2])
                body_index = get_bmi(persons[number_person-1].get_mass(),
                                     persons[number_person-1].get_height())
                print(f'{persons[number_person-1].get_name()}, '
                      f'Ваш индекс массы тела: {round(body_index, 2)}')
                print_scale(body_index)
                recomendation(persons[number_person-1])
        elif action == 4:
            if len(persons) == 0:
                print('Не создано еще ни одного пользователя')
            else:
                number_person = choose_person()
                check_len_start = len(persons)
                del persons[number_person-1]
                check_len_end = len(persons)
                if (check_len_start - check_len_end == 1):
                    print(f'Пользователь {number_person} успешно удален!')
        elif action == 5:
            if len(persons) == 0:
                print('Не создано еще ни одного пользователя')
            else:
                number_person = choose_person()
                body_index = get_bmi(persons[number_person-1].get_mass(),
                                     persons[number_person-1].get_height())
                print(f'{persons[number_person-1].get_name()}, '
                      f'Ваш индекс массы тела: {round(body_index, 2)}')
                print_scale(body_index)
                recomendation(persons[number_person-1]) 

    except ValueError:
        print('*Ошибка! В полях Выбор действия, Рост, Вес, и Возраст, '
              'а также Выбор номера пользователя,\n'
              'необходимо вводить числовые значения. '
              'Эти значения должны быть целыми (кроме поля Вес)')
    except InvalidAction:
        print('*Ошибка! В поле Выбора действия необходимо вводить число '
              'от 0 до 5 включительно')
    except InvalidName:
        print('*Ошибка! Поле ФИО не должно быть пустым или состоять '
              'только из пробелов')
    except InvalidHeight:
        print(f'*Ошибка! Некорректное значение роста: {create_params.height}. '
              'Рост не может быть меньше 0 или больше 300 см.')
    except InvalidMass:
        print(f'*Ошибка! Некорректное значение веса: {create_params.mass}. '
              'Вес не может быть меньше 0 или больше 400 кг.')
    except InvalidAge:
        print(f'*Ошибка! Некорректное значение возраста: {create_params.age}. '
              f'Возраст не может быть меньше 0 или больше 150 лет.')
    except InvalidNumberPerson:
        print('*Ошибка! Введен несуществующий номер пользователя')
