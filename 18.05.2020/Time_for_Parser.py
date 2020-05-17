import Ratomskaya_parser_apache_logs as Parser
import collections
import datetime
import pytz

Parser.main()


dtime_object_set = set()


def translate_f_t_time(list_date):
    for i in list_date:
        dtime = datetime.datetime.strptime(i, '%d/%B/%Y')
        dtime_object_set.add(datetime.datetime.strftime(dtime, '%Y.%m.%d'))
    return dtime_object_set


def print_date_info(date_dict, count_info, string_info):
    print(f'------------------------------------------------',
          f'Информация о дате и {string_info}',
          f'------------------------------------------------')
    count = 0
    for k in date_dict.keys():
        print(f'{k} было зафиксированно запросов от следующих {string_info}:')
        print(f'{date_dict[k]}\n')
        for k2 in date_dict[k].keys():
            count += date_dict[k][k2]

    print(f'Общее кол-во запросов от {string_info} = {count}')
    print(f'Общее кол-во запросов от {string_info} по дням {dict(count_info)}')


print('------------------------------------------------'\
      'Информация о дате и IP-адресах'\
      '------------------------------------------------')
translate_f_t_time(Parser.set_date)
counter_date = collections.Counter()
print(f'Список уникальных дат: {dtime_object_set}')
for date in Parser.list_date:
    counter_date[date] += 1

    
print(f'Количество упоминаний даты: {dict(counter_date)}')
counter_value_date = 0
for value in counter_date.values():
    counter_value_date += value
    
print(f'Общее кол-во дат: {counter_value_date}')
    
#print(len(list_ip_date))
print(f'Кол-во уникальных пар дата-время {len(Parser.set_ip_date)}')

counter_date.clear()

for d in Parser.set_date:
    for ip in Parser.set_ip_date:
        if ip.find(d) != -1:
            counter_date[d] += 1
print(f'Количество уникальных запросов по датам: {dict(counter_date)}')
Parser.save_data('unic_ip_date.txt', Parser.set_ip_date, 'Список уникальных пар IP-дата')

#print(date_brousers)
print_date_info(Parser.date_brousers, Parser.counter_dbrousers, 'десктопных браузерах')

print_date_info(Parser.date_mobale_brousers, Parser.counter_mbrousers, 'мобильных браузерах')

print_date_info(Parser.date_searche_system, Parser.counter_ssystem, 'поисковых систем')

print_date_info(Parser.date_bots, Parser.counter_bots, 'ботов')

time = []
tz = set()
utc = set()
for t in Parser.list_time:
    d_t = datetime.datetime.strptime(Parser.list_time[0], '%d/%B/%Y:%H:%M:%S %z')
    tz.add(str(d_t.tzname()))
    utc.add(str(d_t.utcoffset()))
    time.append(str(d_t))
    
Parser.save_data('date-time_not_string.txt', time, 'Список даты и времени (альтернативная запись)')
print(f'Дата выводится в формате {tz} = {utc}')