import re
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

post = pd.read_csv('data/post_data.csv', index_col=0)

short = pd.read_csv('data/types.csv', index_col=0)


def get_post_index(data):
    try:
        index = re.findall(r'\d{6}', data)
        if len(index) == 1 and len(index[0]) == 6:
            return int(index[0])
    except:
        pass
    return None

def get_post_data(index):
    global post
    try:
        return post.loc[index]
    except:
        pass
    return None

def get_post_index_data(index):
    global post
    try:
        return post.loc[index]
    except:
        pass
    return None



def get_short_data(data):
    global short
    try:
        return short.loc[data]
    except:
        pass
    return None


def get_post_precess(address):
    a = {}
    for k, v in address.items():
        a[k] = '' if v is None else str(v).upper()
    if a['town'] == 'МОСКВА' or a['town'] == 'САНКТ-ПЕТЕРБУРГ':
        a['region'] = a['town']

    if 'word' in a:
        del a['word']
    return a


def get_from_kladr(s, type_search):
    #return list from klad
    pass

def get_found_build_number(s):
    pass