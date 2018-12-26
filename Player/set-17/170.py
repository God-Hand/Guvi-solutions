from collections import Counter
c = Counter(input())
m = max(c.values())
print(m,end=" ")
for k,v in c.items():
    if v==m:
        print(k,end="")
