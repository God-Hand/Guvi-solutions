n = int(input())
l = list(map(int,input().split()))

max = l[0]

for i in l[1:]:
    if max>i:
        break
    max = i
print(max)
