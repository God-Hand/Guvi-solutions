n = input().lower()
from collections import Counter
c = Counter(n)
l = []
for k,v in c.items():
    if v==1:
        l.append(k)

print(" ".join(l))
