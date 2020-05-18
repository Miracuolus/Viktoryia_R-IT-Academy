import datetime

real_time = datetime.datetime.now()

real_time = datetime.datetime.strftime(real_time, '%Y-%m-%d %H:%M:%S.%f')
real_time = real_time[11: 19]