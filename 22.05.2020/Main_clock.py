import datetime
import time
import os
from Number import *


list_numbers = []
for i in range(0, 11):
    list_numbers.append(Number(i))
while True:
    real_time = datetime.datetime.now()
    h = real_time.hour
    m = real_time.minute
    s = real_time.second
    real_time = datetime.datetime.strftime(real_time, '%Y-%m-%d %H:%M:%S.%f')
    real_time = real_time[11: 19]
    for count in range(0, Number.line):
        print(list_numbers[h//10].get_line(count), end=' ')
        print(list_numbers[h%10].get_line(count), end=' ')
        print(list_numbers[10].get_line(count), end=' ')  # разделитель
        print(list_numbers[m//10].get_line(count), end=' ')
        print(list_numbers[m%10].get_line(count), end=' ')
        print(list_numbers[10].get_line(count), end=' ')  # разделитель
        print(list_numbers[s//10].get_line(count), end=' ')
        print(list_numbers[s%10].get_line(count), end=' ')
        print('')
    time.sleep(0.2)
    os.system('cls')  # очистка консоли