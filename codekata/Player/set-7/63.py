n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

i = 0
j = 0
l = []
while i<n and j<n:
    if l1[i] == l2[j]:
        l.append(l1[i])
        i +=1
        j +=1
    elif l1[i] < l2[j]:
        i +=1
    else:
        j +=1

print(*l)
