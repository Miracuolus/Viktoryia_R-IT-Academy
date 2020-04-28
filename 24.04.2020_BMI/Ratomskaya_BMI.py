def bmi(mass, height):
    return round(mass/(height/100)**2, 2)
try:
    mass = float((input('Введите массу тела в кг: ')))
    height = int((input('Введите рост в cм: ')))
    body_index = bmi(mass, height)
    print(f'Ваш индекс массы тела: {body_index}')
    min_index = 16
    max_index = 40
    def scale(index):
        index = round(max(min(index, max_index), min_index))
        left = index - min_index
        right = max_index - index
        return (left, right)
    left, right = scale(body_index)
    print(str(min_index) + '=' * left + '|' + '=' * right +
        str(max_index))
except ValueError:
    print('*Ошибка! Необходимо вводить данные в числовых значениях')



