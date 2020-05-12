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
            'Safari for iPhone': ['iPhone', 'Version', 'Mobile', 'Safari'],}
                      # 'Chrome for iPhone': ['CriOS', 'Mobile', 'Safari']},
            #'iPhone': {'Safari for iPhone': ['Version', 'Mobile', 'Safari'],
                      # 'Chrome for iPhone': ['CriOS', 'Mobile', 'Safari']},
            #'Android': ['Version', 'Mobile', 'Safari'],}
            #'Safari for iPad': ['Version', 'Mobile', 'Safari'],
            #'Chrome for iPad': ['CriOS', 'Mobile', 'Safari']}

count_brousers = {}
for i in brousers.keys():
    count_brousers[i] = 0

all_request_count = 0
unic_ip_addresses = set()

def unic_address(line):
    ip = line.partition(' - - [')
    unic_ip_addresses.add(ip[0])
    return unic_ip_addresses


def list_agents(line):
    agents_with_bots = line.rpartition(') ')
    if agents_with_bots[0] != '':
        agents_without_bots = agents_with_bots[2].rpartition(')')
        if agents_without_bots[2] != '':
            list_brothers = agents_without_bots[2].rsplit(' ')
            if list_brothers != ['"\n']:
                return list_brothers
    #print(line)

def analysis(brousers, request_agents):
    for key in brousers.keys():
        if len(brousers.get(key)) != len(request_agents):
            continue
        is_find = True    
        for agent in brousers.get(key):
            if not find_agent(request_agents, agent):
                is_find = False
                break
        if is_find:    
            count_brousers[key] = count_brousers.get(key) + 1
                
        


def find_agent(agents, value):
    for agent in agents:
        if agent.find(value) != -1:
            return True
    return False




l_count_del = 0
with open(f, 'r') as fp:
    for line in fp.readlines():
        all_request_count += 1
        unic_ip = unic_address(line)
        agents = list_agents(line)
        if agents != None:

            analysis(brousers, agents)
            

            
            l_count_del += 1
    print(l_count_del)
        

    print(f'Количество запросов в файле {f} = {all_request_count}')
    print(f'Количество уникальных запросов в файле {f} = {len(unic_ip)}')
    #print(f'Список уникальных запросов в файле {f}: {unic_ip}')
    #print(f'Количество запросов через браузер Mozilla Firefox в файле {f} = {count_brouser_1}')
    #print(f'Количество запросов через браузер {brouser_2} в файле {f} = {count_brouser_2}')
    #print(f'Количество запросов через браузер {brouser_3} в файле {f} = {count_brouser_3}')
    print(count_brousers)
    num = 0
    for key in count_brousers.keys():
        num += count_brousers.get(key)
    print(num)

    
    
    


    