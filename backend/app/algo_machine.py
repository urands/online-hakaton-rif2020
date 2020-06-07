from algo_func import get_post_index, get_post_data, get_short_data, get_from_kladr


class StateMachine:
    IDLE = 'idle'
    WORD = 'word'
    REGION_TYPE1 = 'region_type1'
    REGION_TYPE = 'region_type'
    REGION_NAME = 'region'
    SUBREGION_TYPE = 'subregion_type'
    SUBREGION_NAME = 'subregion'
    TOWN_TYPE = 'town_type'
    ROUTE_TYPE = 'route_type'
    ROUTE = 'route'
    BUILD_TYPE = 'build_type'
    BUILD = 'build'
    HOUSING_TYPE = 'housing_type'
    HOUSING = 'housing'
    ROOM_TYPE = 'room_type'
    ROOM = 'room'
    TOWN = 'town'
    state = 'idle'
    current = ''
    count = 0

    values = []

    def clear(self):
        self.state = self.IDLE
        self.values = []

    def fill(self,address):
        for v in self.values:
            tst = get_from_kladr(v[1],v[0])
            if tst is None:
                pass
            if v[0] not in address:
                address[v[0]] = v[1]
            else:
                if address[v[0]] is None:
                    address[v[0]] = v[1]
                else:
                    pass
                    #need check doubles aplication

        return address

    def next(self, s, c):
        if c=='':
            return (s,None)
        self.count+=1
        s_t = get_short_data(c)

        #print('-------------------STEP state:',  self.state)
        #if s_t is not None:
        #            print(s_t[0], s_t[1])


        if self.state == self.IDLE or self.state == self.WORD:
            #region parse
            if s_t is None:
                self.state = self.WORD

                #todo: is numeric


                self.values.append((self.WORD, c))
                #print(c)
            else:
                #print('------------->>>>>',s_t[0])
                if len(machine.values) == 0:
                    if s_t[0] == 'region_type':
                        self.state = self.REGION_TYPE1
                        self.values.append((self.REGION_TYPE,s_t[1]))
                if s_t[0] == 'town_type':
                    self.state = self.TOWN_TYPE
                    self.values.append((self.TOWN_TYPE,s_t[1]))
                elif s_t[0] == 'route_type':
                    self.state = self.ROUTE_TYPE
                    self.values.append((self.ROUTE_TYPE,s_t[1]))
                elif s_t[0] == 'build_type':
                    self.state = self.BUILD_TYPE
                    self.values.append((self.BUILD_TYPE,s_t[1]))
                elif s_t[0] == 'room_type':
                    self.state = self.ROOM_TYPE
                    self.values.append((self.ROOM_TYPE,s_t[1]))
                elif s_t[0] == 'housing_type':
                    self.state = self.HOUSING_TYPE
                    self.values.append((self.HOUSING_TYPE,s_t[1]))
                else:
                    if self.state == self.WORD:
                        if s_t is None:
                            print('Need think:', self.values, s, c)
                            pass
                        else:
                            if s_t[0] == 'region_type':
                                self.state = self.REGION_TYPE
                                self.values[0] = (self.REGION_NAME, self.values[0][1])
                                self.values.append((self.REGION_TYPE, s_t[1]))
                                #s_t = [self.REGION_TYPE]
                            if s_t[0] == 'subregion_type':
                                self.state = self.SUBREGION_TYPE
                                self.values[0] = (self.SUBREGION_NAME, self.values[0][1])
                                self.values.append((self.SUBREGION_TYPE, s_t[1]))
                                s_t = [self.SUBREGION_TYPE]



            return (s, s_t)

        if self.state == self.WORD:
            if s_t is None:
                print('Need think:',self.values,s,c)
                pass
            else:
                if s_t[0] == 'region_type':
                    self.state = self.REGION_TYPE
                    self.values[0] = (self.REGION_TYPE, self.values[0][1])
                    self.values.append((self.REGION_NAME, s_t[1]))


        # region parse
        if self.state == self.REGION_TYPE1:
            if s_t is None:
                self.state = self.REGION_TYPE
                self.values.append((self.REGION_NAME, c))
            else:
                pass

        if self.state == self.TOWN_TYPE:
            if s_t is None:
                self.state = self.TOWN
                self.values.append((self.TOWN, c))
                s_t = [self.TOWN]

        if self.state == self.ROUTE_TYPE:
            if s_t is None:
                self.state = self.ROUTE
                self.values.append((self.ROUTE, c))
                s_t = [self.ROUTE]
        if self.state == self.BUILD_TYPE:
            if s_t is None:
                self.state = self.BUILD
                self.values.append((self.BUILD, c))
                s_t = [self.BUILD]
        if self.state == self.ROOM_TYPE:
            if s_t is None:
                self.state = self.ROOM
                self.values.append((self.ROOM, c))
                s_t = [self.ROOM]
        if self.state == self.HOUSING_TYPE:
            if s_t is None:
                self.state = self.HOUSING
                self.values.append((self.HOUSING, c))
                s_t = [self.HOUSING]



        return (s,s_t)





machine = StateMachine()


def algo_reset():
    machine.clear()

def algo_fill(address,d,d_t):
    #print(d,d_t, '-----',d_t[0])
    l = [
        'region_type',
        'subregion_type',
        'town',
        'route',
        'build',
        'room',
        'housing'
    ]

    if d_t[0] in l:

        address = machine.fill(address)
        if d_t[0] == 'housing':
            del address['housing_type']
        machine.clear()


    return address




def algo_state_parser(s, c):
    #try to check index
    #print(s)
    s = s.strip('\'.", ;\n')
    c = c.strip('\'.", ;\n')
    return machine.next(s,c)
