import math
def minPow2Remainder(x):
    if x&(x-1)==0:
        return int(math.log(x,2))
    return minPow2Remainder(x-2**int(math.log(x,2)))
a,b = map(int,input().split())
mult = a*b
print(minPow2Remainder(mult)+1)
