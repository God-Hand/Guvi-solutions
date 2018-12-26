from collections import Counter

n,k = map(int,input().split())
l = list(map(int,input().split()))
c = Counter(l)
c = sorted(filter(lambda x: c[x]<k, c.keys()))
print(*c)
