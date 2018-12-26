n,k = map(int,input().split())
l = list(map(int,input().split()))
k = n - k%n
l = l[k:]+l[:k]
print(*l)
