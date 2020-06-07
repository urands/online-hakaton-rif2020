from algo_func import get_post_index, get_post_data, get_post_precess
from algo_machine import algo_state_parser,algo_fill,algo_reset
import re

def is_nan(x):
    return (x != x)

def address_parse(data_orig):
    data = data_orig.strip(' "\'*(\n')

    address = {
        'index': None,
        'country': 'РОССИЯ',  # Страна Наименование страны (Российская Федерация);
        'region_type': None,  # Регион (область) Наименование субъекта Российской Федерации;
        'region': None,  # Регион (область) Наименование субъекта Российской Федерации;
        'subregion_type': None,  # Тип: район, округ
        'subregion': None,  # Наименование муниципального района, городского округа
        'town_type': None,  # Населенного пункта город, поселок, деревня;
        'town': None,  # Наименование населенного пункта;
        'route_type': None,  # Наименование элемента планировочной структуры;
        'route': None,  # Наименование элемента улично-дорожной сети;
        'build_type': None,  # Тип здания, сооружения или объекта незавершенного строительства;
        'build': None,  # номер здания, сооружения или объекта незавершенного строительства;
        'housing': None,
        # корпус (присваивается зданиям, если некоторые из них не имеют прямого выхода на улицу, то есть находятся во дворе.)
        'subbuild': None,
        # строение ( присваивается зданиям, представляющим единый комплекс и имеющим общий въезд с улицы)
        'room_type': None,  # Тип помещения, расположенного в здании или сооружении.
        'room': None,  # Номер помещения, расположенного в здании или сооружении.
    }



    subset = [d.strip() for d in data.split(',')]


    address['index'] = get_post_index(data)
    if address['index'] is not None:
        post_data = get_post_data(address['index'])
        #print(post_data)
        if post_data is not None:
            address['region_type'] = None if is_nan(post_data['region_type']) else post_data['region_type']
            address['region'] = None if is_nan(post_data['region_name']) else post_data['region_name']
            address['subregion_type'] = None if is_nan(post_data['area_type']) else post_data['area_type']
            address['subregion'] = None if is_nan(post_data['area_name']) else post_data['area_name']
            address['town'] = None if is_nan(post_data['city']) else post_data['city']
        #todo: check data
        data = data.replace(str(address['index']),'')
    #print(address)
    data = data.lower().replace('россия', '')
    data = data.lower().replace('российская федерация', '')
    data = re.split(r' |,|;|\n|\.', data)
    data = [d for d in data if d!='']

    index_current = 0
    algo_reset()
    start = 0
    ret = True
    #print(address)
    #print(data)
    while ret:
        ret=False
        for n in range(start,len(data)):
            #print(n, 'parser:',data[index_current:n])
            d, d_t = algo_state_parser(' '.join(data[index_current:n]), data[n])
            #print(d)
            if d_t is None:
                if n - index_current > 2:
                    #print('Reusage:',n,index_current,  d ,index_current)
                    index_current+=1
                    start=index_current
                    ret = True
                    algo_reset()
                    break
                continue
            address = algo_fill(address,d,d_t)
            #print(address)
            index_current = n+1

    address = get_post_precess(address)



    return address

# parse('Индустриальная ул, дом 2, Подольск, Московская область')
