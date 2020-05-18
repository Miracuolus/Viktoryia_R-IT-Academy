import datetime
import time
from Number import *

while True:
    real_time = datetime.datetime.now()
    real_time = datetime.datetime.strftime(real_time, '%Y-%m-%d %H:%M:%S.%f')
    real_time = real_time[11: 19]
    list_numbers = []
    for number in real_time:
        list_numbers.append(Number(number))
    for value in range(0, len(list_numbers)):
        print(list_numbers[value], end=' ')
    print('\n')
    time.sleep(1)