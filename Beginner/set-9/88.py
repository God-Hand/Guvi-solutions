a,b = map(int,input().split())
for i in range(max(a,b),(a*b)+1):
    if not(i%a) and not(i%b):
        print(i)
        break
