class Scientist:
    def __init__(self, name, field, born, nobel):
        self.name= name
        self.field = field
        self.born= born
        self.nobel= nobel
    def __str__(self):
        return ("{},{},{},{}".format(self.name, self.field,self.born,self.nobel))

import pprint

scientists=(
    Scientist(name ='Ada Lovelace', field ='math', born=1815, nobel=False),
    Scientist(name ='Emmy Noether', field ='math', born=1882, nobel=False),
    Scientist(name ='Marie Curie', field ='physics', born=1867, nobel=True),
    Scientist(name ='Tu Youyou', field ='chemistry', born=1930, nobel=True),
    Scientist(name ='Ada Yonath', field ='chemistry', born=1939, nobel=True),
    Scientist(name ='Vera Rubin', field ='astronomy', born=1928, nobel=False),
    Scientist(name ='Sally Ride', field ='physics', born=1951, nobel=False)
)



list1= [x for x in scientists if x.nobel is True]
from functools import reduce

print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) )



