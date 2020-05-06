class person:
    def __init__(self, second_name, name, father_name, height, mass, age):
        self.__second_name = second_name
        self.__name = name
        self.__father_name = father_name
        self.__height = height
        self.__mass = mass
        self.__age = age

    def __str__(self):
        format_string = '{} {} {}: рост = {}, вес = {}, возраст = {}'
        return format_string.format(self.__second_name, self.__name,\
            self.__father_name, self.__height, self.__mass, self.__age)
        
    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_mass(self):
        return self.__mass

    def set_mass(self, mass):
        self.__mass = mass

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        

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
    print(str(min_index) + '=' * left + '|' + '=' * right + str(max_index))


try:
    mass = float((input('Введите массу тела в кг: ')))
    height = int((input('Введите рост в cм: ')))
    body_index = get_bmi(mass, height)
    print(f'Ваш индекс массы тела: {round(body_index, 2)}')
    print_scale(body_index)
except ValueError:
    print('*Ошибка! Необходимо вводить данные в числовых значениях')
