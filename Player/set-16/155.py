s,k = map(int,input().split())
l = list(map(int,input().split()))
print(*sorted(l[:k]),end=' ')
print(*sorted(l[k:], reverse=True),end=' ')
