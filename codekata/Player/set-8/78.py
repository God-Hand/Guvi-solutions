n,m = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

i = 0;j = 0
while i<n and j<m:
    if l1[i]<=l2[j]:
        print(l1[i], end=' ')
        i+=1
    else:
        print(l2[j], end=' ')
        j+=1
while i<n:
    print(l1[i], end=' ')
    i+=1
while j<m:
    print(l2[j], end=' ')
    j+=1
