s = input()
from collections import Counter

c = Counter(s)
count = 0
for k,v in c.items():
    if k not in ['a','b']:
        count+=v
    if count>1:
        break
if count>1:
    print("no")
else:
    print("yes")
