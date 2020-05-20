import datetime
import time
import os
from Number import *
from Separator import *
import random
import colorama
#from termcolor import colored

colorama.init()
list_numbers = []
for i in range(0, 10):
    list_numbers.append(Number(i))
list_sep = []
for j in range(0, 3):
    list_sep.append(Separator(j))
part = 0
tim_s = 0
style = 36
while True:
    real_time = datetime.datetime.now()
    h = real_time.hour
    m = real_time.minute
    s = real_time.second
    if tim_s != s:
        style = random.randint(31, 36)
    print('\33[' + str(style) + 'm')
    part += 1
    for count in range(0, Number.line):
        print(list_numbers[h//10].get_line(count), end=' ')
        print(list_numbers[h%10].get_line(count), end=' ')
        print(list_sep[part%len(list_sep)].get_line(count), end=' ')  # разделитель
        print(list_numbers[m//10].get_line(count), end=' ')
        print(list_numbers[m%10].get_line(count), end=' ')
        print(list_sep[len(list_sep) - 1 - part%len(list_sep)].get_line(count), end=' ')  # разделитель
        print(list_numbers[s//10].get_line(count), end=' ')
        print(list_numbers[s%10].get_line(count), end=' ')
        print('')
    time.sleep(0.5)
    tim_s = s
    os.system('cls')  # очистка консоли