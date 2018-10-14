a,b = map(int,input().split())
for i in range(min(a,b),0,-1):
    if not(a%i) and not(b%i):
        print(i)
        break
