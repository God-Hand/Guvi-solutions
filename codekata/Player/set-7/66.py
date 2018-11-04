from collections import Counter
n,k = map(int,input().split())
l = Counter(list(map(int,input().split())))

for key,v in l.items():
    if v==k:
        print(key)
