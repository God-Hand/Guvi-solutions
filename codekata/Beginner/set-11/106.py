import functools
s,n = map(int,input().split())
l = list(filter(lambda x: x%2, list(map(int,input().split()))))
print(l[n-1])
