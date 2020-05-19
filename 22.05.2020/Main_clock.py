import datetime
import time
import os
from Number import *
import random
import colorama
from termcolor import colored

colorama.init()
list_numbers = []
for i in range(0, 11):
    list_numbers.append(Number(i))
while True:
    style = random.randint(31, 36)
    print('\33[' + str(style) + 'm')
    print('\033[6m')
    real_time = datetime.datetime.now()
    h = real_time.hour
    m = real_time.minute
    s = real_time.second
    for count in range(0, Number.line):
        print(list_numbers[h//10].get_line(count), end=' ')
        print(list_numbers[h%10].get_line(count), end=' ')
        print('\33[6m', list_numbers[10].get_line(count), end=' ')  # разделитель
        print(list_numbers[m//10].get_line(count), end=' ')
        print(list_numbers[m%10].get_line(count), end=' ')
        print(list_numbers[10].get_line(count), end=' ')  # разделитель
        print(list_numbers[s//10].get_line(count), end=' ')
        print(list_numbers[s%10].get_line(count), end=' ')
        print('')
    time.sleep(1)
    os.system('cls')  # очистка консоли