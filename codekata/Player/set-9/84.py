n = int(input())
l = list(map(int,input().split()))
max = 0

for i in range(n):
    for j in range(i,n):
        x = i|j
        if x>max:
            max = x
print(max)

