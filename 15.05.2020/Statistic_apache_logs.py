f = 'apache_logs.txt'
with open(f, 'r') as fp:
    count = 0
    ip_addresses = set()
    for line in fp.readlines():
        count += 1
        ip = line.partition(' - - [')
        ip_addresses.add(ip[0])

    print(f'Количество запросов в файле {f} = {count}')
    print(f'Количество уникальных запросов в файле {f} = {len(ip_addresses)}')
    print(f'Список уникальных запросов в файле {f}: {ip_addresses}')


    