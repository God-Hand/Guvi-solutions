import math as m

s,e = map(int,input().split())
for n in range(s+1,e):
    p = len(str(n))
    sum=0
    for i in str(n):
        sum+=m.pow(int(i),p)

    if sum==n:
        print(n)
