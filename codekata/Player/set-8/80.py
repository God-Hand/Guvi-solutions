n = int(input())
l = sorted(list(map(int,input().split())))

import sys
min = sys.maxsize
for i in range(1,n):
    if l[i] - l[i-1] < min:
        min = l[i] - l[i-1]
print(min)
