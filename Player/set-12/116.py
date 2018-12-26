n = int(input())
l = list(map(int,input().split()))
d = {}
for i in l:
    try:
        d[i] +=1
    except:
        d[i] = 1
d2 = sorted(d, key=d.get, reverse=True)
print(d2)
