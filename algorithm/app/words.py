from enum import Enum
from algo_func import get_short_data
import determinant as det


class GeoType(Enum):
    index = 'index'
    country = 'country' # Страна Наименование страны (Российская Федерация);
    region_type = 'region_type' # Регион (область) Наименование субъекта Российской Федерации;
    region = 'region' # Регион (область) Наименование субъекта Российской Федерации;
    subregion_type = 'subregion_type' # Тип: район, округ
    subregion = 'subregion' # Наименование муниципального района, городского округа
    town_type = 'town_type'  # Населенного пункта город, поселок, деревня;
    town = 'subregion' # Наименование населенного пункта;
    route_type = 'route_type'  # Наименование элемента планировочной структуры;
    route = 'route'  # Наименование элемента улично-дорожной сети;
    build_type = 'build_type'  # Тип здания, сооружения или объекта незавершенного строительства;
    build = 'build'  # номер здания, сооружения или объекта незавершенного строительства;
    housing = 'housing'
    # корпус (присваивается зданиям, если некоторые из них не имеют прямого выхода на улицу, то есть находятся во дворе.)
    subbuild = 'subbuild'
    # строение ( присваивается зданиям, представляющим единый комплекс и имеющим общий въезд с улицы)
    room_type  = 'room_type' # Тип помещения, расположенного в здании или сооружении.
    room = 'room'  # Номер помещения, расположенного в здании или сооружении.



    @classmethod
    def keys(cls):
        for name, member in cls.__members__.items():
            yield name

    @classmethod
    def with_commas(cls):
        return ['region_type', 'subregion_type', 'town_type', 'route_type', 'build_type', 'room_type']

    @classmethod
    def with_text(cls):
        return ['region', 'subregion','town_type', 'town', 'route_type', 'build_type', 'room_type']





class Word(object):
    idx = None
    word = None
    full = None
    align = None

    def __init__(self, idx, word):
        self.idx = idx
        self.word = word.strip()
        self.probable = {k: 0 for k in GeoType.keys()}
        if self.word[-1] == ',':
            self.word = self.word[:-1]
            self.align = 'right'


        if len(self.word) >0 and self.word[-1] == '.':
            self.word = self.word[:-1]
            self.update_propable(GeoType.with_commas(),0.1)

        word_type = det.WordType.get_type(self.word)

        if word_type == det.WordType.build.value:
            self.update_propable(GeoType.build.value, 0.5)

        if word_type == det.WordType.index.value:
            self.update_propable(GeoType.index.value, 0.8)

        if word_type == det.WordType.ruchar.value:
            self.update_propable(GeoType.with_text(),0.2)

        short = get_short_data(self.word)
        print(word_type, word,short)




    def __repr__(self):
        return f'<{self.word}:{self.align}:{self.type}>'

    @property
    def type(self):
        return max(self.probable, key=self.probable.get)


    def update_propable(self,keys, value):
        print(keys,value)
        if type(keys) == list:
            for k in keys:
                self.probable[k] += value
        elif type(keys) == str:
            self.probable[keys] += value



