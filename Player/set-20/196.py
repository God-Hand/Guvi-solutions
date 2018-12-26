from collections import Counter
n = int(input())
l = map(int,input().split())
c = Counter(l)
print(*list(filter(lambda x:c[x]==1,c.keys)))
