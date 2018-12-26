n = int(input())
l = list(map(int,input().split()))
num = l[0]
counter = 1
max = 1

for i in l[1:]:
    if i==num:
        counter +=1
    else:
        num = i
        counter = 1
    if max < counter:
        max = counter
print(max)
