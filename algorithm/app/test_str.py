
from algo import address_parse


s = 'Московская область, г.БАЛАШИХА, Маяковского, дом 16, корп. а'



print(s)

address = address_parse(s)

print(address)

m = ['' if v is None else str(v) for k, v in address.items()]
m = ';'.join(m)
# print('orig:',line)
# print('decod:',m)
# if (n % 2) == 0:
print(m)