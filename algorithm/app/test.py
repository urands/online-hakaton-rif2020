
from algo import address_parse


def is_nan(x):
    return (x != x)


def read_from_file(filename='data/bad_ansi.csv', num=10, skip = 6):
    n = 0
    index_cnt = 0
    fw = open('../../bad_conv.csv','w')

    with open(filename) as f:
        for line in f:
            n += 1
            if n<skip:
                continue
            if num is not None and n-skip > num:
                break
            data = line.split(';')
            address = address_parse(data[1])

            m = [ v for k, v in address.items()]
            m = ';'.join(m)
            #print('orig:',line)
            #print('decod:',m)
            #if (n % 2) == 0:
            print(n)

            fw.write(line.strip())
            fw.write(';')
            fw.write(m)
            fw.write('\n')

            if address is not None:
                #print(type(address['index']))
                if (address['index'] is not None) and address['index']!='' and (int(address['index']) >= 100999):
                    index_cnt+=1


            #m = [ v for k,v in address.iteritems()]
            #print(address)
            #print( m )


            #print(line, address)
    fw.close()
    print('Total=',n, 'index=',index_cnt, index_cnt/n*100)




read_from_file(num=None, skip=0)