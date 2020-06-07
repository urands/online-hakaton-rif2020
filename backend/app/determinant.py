import re
from enum import Enum

class WordType(Enum):
    ruchar = 'ruchar'
    numbers = 'numbers'
    build = 'build'
    numsym = 'numsym'
    index = 'index'

    @classmethod
    def get_type(cls,s):
        if re.match(r'^[А-я]+$', s) is not None:
            return cls.ruchar.value
        if re.match(r'^\d{6}$', s) is not None:
            return cls.index.value
        if re.match(r'^\d+$', s) is not None:
            return cls.numbers.value
        if re.match(r'^\d{1,4}[А-я]$', s) is not None:
            return cls.build.value
        if re.match(r'^\d{1,4}[А-я]?/\d{1,4}[А-я]?$', s) is not None:
            return cls.build.value


print(WordType.get_type('16/3443ф'))