from collections import Counter
n = input()
c = Counter(n)
l = list(filter(lambda x: c[x]>1, c.keys()))
n2 = ''
for i in n:
    if i in l:
        n2+=i.upper()
    else:
        n2+=i
print(n2)
