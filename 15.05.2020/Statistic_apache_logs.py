f = 'apache_logs.txt'
with open(f, 'r') as fp:
    count = 0
    for line in fp.readlines():
        count += 1
    print(f'Количество запросов в файле {f} = {count}')

    