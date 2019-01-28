n = int(input())
l = list(map(int,input().split()))

max_count = 1
count = 1
for i in range(1,n):
    if l[i] >= l[i-1]:
        count += 1
    elif max_count < count:
        max_count = count
        count = 1

print(max_count)
