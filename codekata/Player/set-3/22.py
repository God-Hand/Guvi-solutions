n,m = map(int,input().split())
for i in range(min(n,m),0,-1):
    if not(n%i) and not(m%i):
        print(i)
        break
