n = int(input())
l = list(map(int,input().split()))
import sys
min = sys.maxsize
max = 0
for i in l:
    if max<i:
        max = i
    if min > i:
        min = i
print(max-min)
