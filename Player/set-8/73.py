n,k = map(int,input().split())
l = list(map(int,input().split()))

for i in range(n):
    if l[i] == k:
        print(i+1)
        break
