f = 'apache_logs.txt'
brouser_1 = 'Safari'
brouser_2 = 'Firefox'
brouser_3 = 'Chrome'

with open(f, 'r') as fp:
    count = 0
    count_brouser_1 = 0
    count_brouser_2 = 0
    count_brouser_3 = 0
    ip_addresses = set()
    for line in fp.readlines():
        count += 1
        ip = line.partition(' - - [')
        ip_addresses.add(ip[0])
        if line.find(brouser_1) != -1:
            count_brouser_1 += 1
        if line.find(brouser_2) != -1:
            count_brouser_2 += 1
        if line.find(brouser_3) != -1:
            count_brouser_3 += 1


    print(f'Количество запросов в файле {f} = {count}')
    print(f'Количество уникальных запросов в файле {f} = {len(ip_addresses)}')
    print(f'Список уникальных запросов в файле {f}: {ip_addresses}')
    print(f'Количество запросов через браузер {brouser_1} в файле {f} = {count_brouser_1}')
    print(f'Количество запросов через браузер {brouser_2} в файле {f} = {count_brouser_2}')
    print(f'Количество запросов через браузер {brouser_3} в файле {f} = {count_brouser_3}')
    


    