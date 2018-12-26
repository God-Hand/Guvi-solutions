import math
pos = 0
def minPow2(x):
    if x==1 or x==0:
        return x
    return x%2 + minPow2(x//2)
    
    
a,b = map(int,input().split())
mult = a|b
print(minPow2(mult))
