n,m = map(int,input().split())
t = list(map(int,input().split()))
d = dict()
for i in range(n):
    if t[i] not in d.keys():
        d[t[i]] = 1
    else :
        d[t[i]] += 1

for i in range(n,n+m):
    try:
        d[t[i]] -= 1
    except:
        d[t[i]] = -1

def rem(p):
    if p[1]==0:
        return True
f = filter(rem, d.items())

print(*(x for x,v in sorted(f)))
