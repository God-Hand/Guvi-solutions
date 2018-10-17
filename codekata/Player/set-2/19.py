import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if not n%i:
            return False
    return True

n = int(input())
for i in range(2,n//2+1):
    if not n%i and isPrime(i):
        print(i,end=" ")
