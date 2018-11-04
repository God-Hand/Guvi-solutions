n = int(input())
l = list(map(int,input().split()))
arr = l[0]

for i in range(1,n):
    arr = arr ^ l[i]
print(arr)
