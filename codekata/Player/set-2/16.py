import operator
n = int(input())
l = list(map(int,input().split()))
d = dict([])
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
sorted_d = list(sorted(d.items(),key=operator.itemgetter(1)))
print((sorted_d[0])[0])
