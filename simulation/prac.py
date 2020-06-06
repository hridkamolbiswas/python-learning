class cal:

    def __init__(self, name):
        self.name = name
        self.add = 'hamm'


def use_class(cal):
    print(cal.name, cal.add)

ob = cal('hrid')
#print(ob.name, ob.add)
use_class(ob)
class Sim:
    def __init__(self):
        self.n_driving=[]
        self.parking=[]


s = []
name = 'hrid'

while True:
    print('after while')
    if name == 'hrid':
        print('iam hrid')
    if not s:
        print('im empty')
        continue