n = int(input())
l = list(map(int,input().split()))

s = 0
for i in range(1,n):
    s+=max(l[i],l[i-1])
print(s)
