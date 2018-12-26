n,k = map(int,input().split())
l = sorted(list(map(int,input().split())))

for i in l:
    if i >= k:
        break
    print(i,end=' ')
