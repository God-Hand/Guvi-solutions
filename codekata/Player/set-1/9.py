import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if not n%i:
            return False
    return True

l,r = map(int,input().split())
count = 0
for i in range(l,r+1):
    if isPrime(i):
        count+=1

print(count)
