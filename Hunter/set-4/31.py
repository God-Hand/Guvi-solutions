n = int(input())
l = list(map(int,input().split()))
p = 1
l2 = []
for i in l:
    if i<0:
        l2.append(i)
    elif i>0:
        p *= i

l2 = list(sorted(l2, reverse=True))
if len(l2)%2:
    l2 = l2[1:]

    p *= i

print(p)

