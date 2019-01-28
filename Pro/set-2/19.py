def merge(l1, l2):
    i = 0
    j = 0
    l = []
    while i != len(l1) and j != len(l2):
        if l1[i] <= l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j+=1
    while i!=len(l1):
        l.append(l1[i])
        i+=1
    while j!=len(l2):
        l.append(l2[j])
        j+=1
    return l

k  = int(input())
l = []
total = 0
for i in range(k):
    l.append(list(map(int,input().split())))
    total += len(l[-1])

final = []
while len(l) != 1:    
    final = []
    k = len(l)
    for i in range(0,k,2):
        if i == k-1:
            final.append(l[i])
        else:
            final.append(merge(l[i], l[i+1]))
    l = final

l = l[0]
print(*l)
