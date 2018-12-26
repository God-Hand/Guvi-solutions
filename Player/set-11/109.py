n = int(input())
l = list(map(int,input().split()))
for i in range(n):
    print(sum(l[i:]), end=' ')
