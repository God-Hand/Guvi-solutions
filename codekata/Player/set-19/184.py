n = int(input())
l = sorted(list(map(int,input().split())))
count=0
for i in range(n):
    if i+1 != l[i]:
        count+=abs(l[i]-i-1)
print(count)
