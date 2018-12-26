import math
from collections import Counter
b = input()
c = Counter(b)
if c['1']==1:
    print(int(b,2))
else:
    print(2**(len(b)))
