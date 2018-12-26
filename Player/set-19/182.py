from collections import Counter
n = int(input())
l = list(map(int,input().split()))
c = Counter(l)
ll = list(filter(lambda x: c[x]>1,c.keys()))
count = 0
for i in ll:
    count+=c[i]
print(count)
