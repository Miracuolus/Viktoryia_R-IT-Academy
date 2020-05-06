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
