n = int(input());s=0
l = list(map(int,input().split()))
for i in range(1,n):
    s += l[i]+l[i-1]
print(s)
