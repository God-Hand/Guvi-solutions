import math as m
n,q = map(int,input().split())
for j in range(n+1,q):
    flag = True
    for i in range(2,int(m.sqrt(j))+1):
        if not(j%i):
            flag = False
            break
    if flag:
        print(j, end=' ')
