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
                                    self.__father_name, self.__height,
                                    self.__mass, self.__age)

    def get_second_name(self):
        return self.__second_name

    def get_name(self):
        return self.__name

    def get_father_name(self):
        return self.__father_name

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
