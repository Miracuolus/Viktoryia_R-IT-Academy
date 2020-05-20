import datetime
import time
import os
from Number import *
import random
import colorama
#from termcolor import colored

colorama.init()
list_numbers = []
for i in range(0, 12):
    list_numbers.append(Number(i))
part1 = 1
part2 = 1
while True:
    real_time = datetime.datetime.now()
    h = real_time.hour
    m = real_time.minute
    s = real_time.second
    style = random.randint(31, 36)
    print('\33[' + str(style) + 'm')
    for count in range(0, Number.line):
        print(list_numbers[h//10].get_line(count), end=' ')
        print(list_numbers[h%10].get_line(count), end=' ')
        if part1 == 1:
            print(list_numbers[10].get_line(count), end=' ')  # разделитель
            part1 = 2
        elif part1 == 2:
            print(list_numbers[11].get_line(count), end=' ')  # разделитель
            part1 = 1
        print(list_numbers[m//10].get_line(count), end=' ')
        print(list_numbers[m%10].get_line(count), end=' ')
        if part2 == 1:
            print(list_numbers[11].get_line(count), end=' ')  # разделитель
            part2 = 2
        elif part2 == 2:
            print(list_numbers[10].get_line(count), end=' ')  # разделитель
            part2 = 1
        print(list_numbers[s//10].get_line(count), end=' ')
        print(list_numbers[s%10].get_line(count), end=' ')
        print('')
    time.sleep(0.5)
    os.system('cls')  # очистка консоли