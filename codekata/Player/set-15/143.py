d = dict()
n = int(input())
l = list(map(int,input().split()))
dl = list(map(int,input().split()))

for i in range(n):
    d[dl[i]] = l[i]

dl.sort()
for i in range(n):
    print(d[dl[i]],end=" ")
