import math
pos = 0
def minPow2Remainder(x):
    if x==1 or x==0:
        return x
    return x%2 + minPow2Remainder(x//2)
    
    
a,b = map(int,input().split())
mult = a|b
print(minPow2Remainder(mult))
