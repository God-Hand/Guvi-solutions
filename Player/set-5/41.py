n,k = map(int,input().split())
for i in range(n//k):
    if k**i == n:
        print("yes")
        break
    elif k**i>n:
        print("no")
        break
