import math
import os
import random
import re
import sys

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*s) for s in OrderedCounter(sorted(input())).most_common(3)]


if __name__ == '__main__':
    s = input()