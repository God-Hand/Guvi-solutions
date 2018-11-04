n,k,p = map(int,input().split())
l = []
while n>0:
    x = n%10
    n = n//10
    l.append(x)

print(l[-(k+p)])
