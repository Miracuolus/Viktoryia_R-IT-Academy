f = 'apache_logs.txt'
brousers = {'Mozilla Firefox' : ['Gecko', 'Firefox'],
            'Mozilla Firefox2' : ['Gecko', 'BonEcho'],
            'Mozilla for Linux' : ['Gecko', 'Firefox', 'Iceweasel'],
            'Google Chrome': ['Chrome', 'Safari'],
            'Apple Safari': ['Version', 'Safari'],
            'Opera 19': ['Chrome', 'Safari', 'OPR'],
            'Opera 12': ['Presto', 'Version'],
            'Opera 9': ['Presto'],
            'Internet Explorer': ['like', 'Gecko'],
            'Microsoft Edge': ['Chrome', 'Safari', 'Edge'],
            'Bing': ['BingPreview'],
            'Chromium' : ['Ubuntu', 'Chromium', 'Chrome', 'Safari'],
            'Safari for iPhone': ['Version', 'Mobile', 'Safari'],
            'Chrome for iPhone': ['CriOS', 'Mobile', 'Safari'],
            'Android': ['Version', 'Mobile', 'Safari'],
            'Safari for iPad': ['Version', 'Mobile', 'Safari'],
            'Chrome for iPad': ['CriOS', 'Mobile', 'Safari']}

count_brousers = {}
for i in brousers.keys():
    count_brousers[i] = 0
    

count = 0
count_brouser_1 = 0
ip_addresses = set()

def agents(line):
    user_agent = line.rpartition(') ')
    if user_agent[0] != '':
        #print(user_agent[2])
        agent = user_agent[2].rpartition(')')
        #print(agent)
        if agent[2] != '':
            #print(agent[2])
            value_brothers = agent[2].rsplit(' ')
            if value_brothers != ['"\n']:
                #print(value_brothers)
            #if value_brothers == None:
                #print(line)
                #print(value_brothers)
                return value_brothers
    #print(line)



with open(f, 'r') as fp:
    co = []
    c = 0
    t = 0
    l_count_del = 0
    for line in fp.readlines():
        count += 1
        ip = line.partition(' - - [')
        ip_addresses.add(ip[0])
        l_brouthers = agents(line)
        if l_brouthers != None:
            for k in brousers.keys():
                len(brousers.get(k))
                c = 0
                t = 0
                for v in brousers.get(k):
                    if type(l_brouthers) == list:
                        if len(l_brouthers) == len(brousers.get(k)):
                            for iii in l_brouthers:
                                if iii.find('Mobile') != 1:
                                    if (iii.find(v) != -1) and (line.find(k) != -1):
                                        t += 1
                                elif iii.find(v) != -1:
                                    t += 1
                if t == len(brousers.get(k)):
                    count_brousers[k] = count_brousers.get(k) + 1
            l_count_del += 1
    print(l_count_del)
        

    print(f'Количество запросов в файле {f} = {count}')
    print(f'Количество уникальных запросов в файле {f} = {len(ip_addresses)}')
    #print(f'Список уникальных запросов в файле {f}: {ip_addresses}')
    print(f'Количество запросов через браузер Mozilla Firefox в файле {f} = {count_brouser_1}')
    #print(f'Количество запросов через браузер {brouser_2} в файле {f} = {count_brouser_2}')
    #print(f'Количество запросов через браузер {brouser_3} в файле {f} = {count_brouser_3}')
    print(count_brousers)
    num = 0
    for key in count_brousers.keys():
        num += count_brousers.get(key)
    print(num)

    
    
    


    