class Person:
    def __init__(self, second_name, name, father_name, height, mass, age):
        self.__second_name = second_name
        self.__name = name
        self.__father_name = father_name
        self.set_height(height)
        self.set_mass(mass)
        self.set_age(age)

    def __str__(self):
        format_string = '{} {} {}: рост = {}, вес = {}, возраст = {}'
        return format_string.format(self.__second_name, self.__name,
            self.__father_name, self.__height, self.__mass, self.__age)

    def get_second_name(self):
        return self.__second_name

    def get_name(self):
        return self.__name

    def get_father_name(self):
        return self.__father_name

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height <= 0 or height >= 300:
            raise InvalidHeight
        self.__height = height

    def get_mass(self):
        return self.__mass

    def set_mass(self, mass):
        if mass <= 0 or mass >= 400:
            raise InvalidMass
        self.__mass = mass

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0 or age > 150:
            raise InvalidAge
        self.__age = age


class InvalidHeight(Exception):
    """Класс ошибки при вводе невалидного роста"""
    pass


class InvalidMass(Exception):
    """Класс создания ошибки при вводе невалидной массы тела"""
    pass


class InvalidAge(Exception):
    """Класс создания ошибки при вводе невалидного возраста"""
    pass
