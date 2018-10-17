def isSurround(l,i,j):
    if l[i][j]=='1' and l[i][j-1]=='0' \
       and l[i][j+1]=='0' and l[i-1][j]=='0' \
       and l[i+1][j]=='0':
        return 1
    return 0

    
n = int(input())
l = [['0']*(n+2)]
for _ in range(n):
    l += [['0']+list(input())+['0']]
l += [['0']*(n+2)]
count = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        count+=isSurround(l,i,j)

print(count)
