n = int(input())
l = list(map(int,input().split()))
d = {l[i] : i+1 for i in range(n)}
print(*(d[i] for i in sorted(l)))
