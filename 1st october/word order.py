from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for x in range(int(input())))
print(len(d))
print(*d.values())