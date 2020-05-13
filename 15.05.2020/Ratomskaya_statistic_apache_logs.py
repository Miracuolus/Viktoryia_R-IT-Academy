import re

f = 'apache_logs.txt'
brousers = {'Mozilla Firefox' : ['Gecko', 'Firefox'],
            'Mozilla Firefox2' : ['Gecko', 'BonEcho'],
            'Mozilla for Linux' : ['Gecko', 'Firefox', 'Iceweasel'], #94
            'Google Chrome': ['Chrome', 'Safari'],
            'Apple Safari': ['Version', 'Safari'],
            'Opera 19': ['Chrome', 'Safari', 'OPR'], #19
            'Opera 12': ['Presto', 'Version'],#89
            'Opera 9': ['Presto'], #89
            'Internet Explorer': ['like', 'Gecko'],
            'Microsoft Edge': ['Chrome', 'Safari', 'Edge'],
            'Bing': ['BingPreview'], #8
            'Chromium' : ['Ubuntu', 'Chromium', 'Chrome', 'Safari'],} #176

mobile_brousers = {'Safari on iPhone': ['(iPhone', 'Version', 'Mobile', 'Safari'],
                   'Chrome on iPhone': ['(iPhone','CriOS', 'Mobile', 'Safari'],
                   'Chrome on Android': ['Android', 'Chrome', 'Mobile', 'Safari'],
                   'Others on Android': ['Android', 'Version', 'Mobile', 'Safari'],
                   'Safari on iPad': ['(iPad', 'Version', 'Mobile', 'Safari'],
                   'Chrome on iPad': ['(iPad','CriOS', 'Mobile', 'Safari']}

search_systems = {'Яндекс': 'http://yandex.com/bots',
                  'Google': 'http://www.google.com/bot.html',
                  'Bing': 'http://www.bing.com/bingbot.htm',
                  'Yahoo! Slurp': 'http://help.yahoo.com/help/us/ysearch/slurp',
                  'Mail.ru': 'http://go.mail.ru/help/robots'}

bots = {'Ahrefs': 'http://ahrefs.com/robot/',
        'Majestic': 'http://www.majestic12.co.uk/bot.php?+',
        'Exabot': 'http://www.exabot.com/go/robot',
        'Heritrix': 'http://www.archive.org/details/archive.org_bot)'}

count_brousers = {}
for i in brousers.keys():
    count_brousers[i] = 0
for j in mobile_brousers.keys():
    count_brousers[j] = 0

count_search = {}
for k in search_systems.keys():
    count_search[k] = 0

count_bots = {}
for g in bots.keys():
    count_bots[g] = 0

all_request_count = 0
unic_ip_addresses = set()

pattern_unic_address = re.compile(r' - - ')
pattern_times = re.compile(r'\d+\/\w+\/\d+\:\d+\:\d+\:\d+')

def pattern_protocols():
    protocol = pattern_unic_address.split(line)
    protocol = pattern_times.split(protocol[1])
    protocol = re.split(r'\s\+\d+\]\s\"', protocol[1])
    protocol = re.split(r'\s\"', protocol[1], maxsplit=1)
    return protocol

def pattern_system():
    system = pattern_protocols()
    if system[1][0] == '-':
        sys = re.split(r'\-\s\"', system[1])
    else:
        sys = re.split(r'\w+.+\"\s\"', system[1])
    return sys

def pattern_agents():
    agents = pattern_system()
    if len(agents) == 2:
       agent = re.split(r'\w+\/.+\s\(.+\)\s', agents[1]) 
    else:
       agent = re.split(r'\w+\/.+\s\(.+\)\s', agents[0])
    return agent

def unic_address(line):
    ip = pattern_unic_address.split(line)
    unic_ip_addresses.add(ip[0])
    return unic_ip_addresses


list_time = []
def time(line):
    time = pattern_times.findall(line)
    list_time.append(time[0])
    return list_time

list_protocol = []
def protocol(line):
    protocol = pattern_protocols()
    list_protocol.append(protocol[0])
    return list_protocol

list_referers = []
not_url = 0

def referer():
    protocol = pattern_protocols()
    if protocol[1][0] == '-':
        global not_url
        not_url += 1
    else:
        list_referer = re.findall(r'\w+.+\"\s\"', protocol[1])
        list_referers.append(list_referer[0])
    
list_system = []
no_inform_syst = 0   
def system():
    sys = pattern_system()
    if len(sys) == 2:
       system = re.findall(r'\w+\/.+\s\(.+\)\s', sys[1]) 
    else:
       system = re.findall(r'\w+\/.+\s\(.+\)\s', sys[0])
    if system == []:
        global no_inform_syst
        no_inform_syst += 1
    else:
        list_system.append(system[0])

list_agent = []
list_bots_research = []
def agents():
    global list_agent
    agent = pattern_agents()
    if len(agent) == 2:
        agents = re.findall(r'\w+.+\n', agent[1]) # браузеры и поиск 
        if re.findall(r'\w+\:\/+\w+\.\w+.+\n', agent[1]):
            agents = re.findall(r'\w+\:\/+\w+\.\w+.+\n', agent[1])
            list_bots_research.append(agents[0])
            agents = re.split(r'\w+\:\/+\w+\.\w+.+\n', agent[1])
            agents = re.split(r'\(.+', agent[1])
            list_agent = agents[0].split(' ') # браузеры
            return list_agent
                        
        else:
            if agents != []:
                list_agent = agents[0].split(' ') # браузеры
                return list_agent

    else:
       agents = re.findall(r'\w+\:\/+\w+\.\w+.+\n', agent[0]) # боты
       if agents != []:
           list_bots_research.append(agents[0])
           return list_agent
    

def list_agents(line):
    agents_with_bots = line.rpartition(') ')
    if agents_with_bots[0] != '':
        agents_without_bots = agents_with_bots[2].rpartition(')')
        if agents_without_bots[2] != '':
            list_brothers = agents_without_bots[2].rsplit(' ')
            if list_brothers != ['"\n']:
                return list_brothers
    #print(line)

request_agents = []
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

def analysis_mobile(brousers, line):
    for key in brousers.keys():
        is_find = True    
        for agent in brousers.get(key):
            if line.find(agent) == -1:
                is_find = False
                break
        if is_find:    
            count_brousers[key] = count_brousers.get(key) + 1

def analysis_search_systems(count, brousers, line):
    for key in brousers.keys():
        is_find = True    
        if line.find(brousers[key]) == -1:
            is_find = False
            continue
        if is_find:    
            count[key] = count.get(key) + 1

               
     
def find_agent(agents, value):
    for agent in agents:
        if agent.find(value) != -1:
            return True
    return False




l_count_del = 0
with open(f, 'r') as fp:
    for line in fp.readlines():
        all_request_count += 1 # кол-во запросов

        unic_ip = unic_address(line) # список уникальных IP

        time(line) # список даты и времени
        
        protocol(line) # список протоколов
        
        referer() # список URL-запросов

        system() # информация о системе

        analysis_mobile(mobile_brousers, line)
        analysis_search_systems(count_search,search_systems, line)
        analysis_search_systems(count_bots,bots, line)

        agent = agents()
        if agent != None:
            #print(agent)
            l_count_del += 1
        
        analysis(brousers, list_agent)
        
        #print(len(list_bots_research))
        
        #agents = list_agents(line)
        #analysis_search_systems(search_systems, line)
        #analysis_search_systems(bots, line)
        #if agents != None:

        #    if find_agent(agents, 'Mobile'):
                
        #        analysis_mobile(mobile_brousers, line)
        #    else:
        #        analysis(brousers, agents)
            

            
        #    l_count_del += 1
  
    set_bots_research = set()
    for i in list_bots_research:
        bot = re.split(r'\"\n', i)
        bot = re.split(r'\;', bot[0])
        bot = re.split(r'\)', bot[0])
        set_bots_research.add(bot[0])
    #print(set_bots_research)
    print(len(set_bots_research))
    print(f'Количество запросов в файле {f} = {all_request_count}')
    print(f'Количество уникальных запросов в файле {f} = {len(unic_ip)}')
    print(f'Нет URL-запроса: {not_url}')
    print(f'Кол-во URL-запроса: {len(list_referers)}')
    print(f'Нет информации от системе: {no_inform_syst}')
    #print(f'Список уникальных запросов в файле {f}: {unic_ip}')
    #print(f'Количество запросов через браузер Mozilla Firefox в файле {f} = {count_brouser_1}')
    #print(f'Количество запросов через браузер {brouser_2} в файле {f} = {count_brouser_2}')
    #print(f'Количество запросов через браузер {brouser_3} в файле {f} = {count_brouser_3}')
    print(count_brousers)
    num = 0
    for key in count_brousers.keys():
        num += count_brousers.get(key)
    print(num)

    print(count_search)
    num2 = 0
    for key in count_search.keys():
        num2 += count_search.get(key)
    print(num2)

    print(count_bots)
    num3 = 0
    for key in count_bots.keys():
        num3 += count_bots.get(key)
    print(num3)

    
    
    


    