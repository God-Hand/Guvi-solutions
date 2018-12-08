n = int(input())
previous = 100001
l = list(map(int,input().split()))
for i in range(n):
    x = l[i]
    if not x%previous:
        print(x,end=" ")
    previous = x
