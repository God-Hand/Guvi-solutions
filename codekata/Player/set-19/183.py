n = int(input())
l = list(map(int,input().split()))
count=0
for i in range(n):
    if i+1 != l[i]:
        count+=1
print(count)
