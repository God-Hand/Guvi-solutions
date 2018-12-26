n,m = map(int,input().split())
for i in range(max(n,m),100000):
    if not(i%n) and not(i%m):
        print(i)
        break
    
