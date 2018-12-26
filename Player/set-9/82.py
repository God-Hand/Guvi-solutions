n = int(input())
l = list(map(int,input().split()))
arr = l[0]

for i in range(1,n):
    arr &= l[i]
print(arr)
