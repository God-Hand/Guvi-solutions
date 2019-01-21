from math import sqrt

def isPrime(n):
    if not n%2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if not n%i:
            return False
    return True

n = int(input())
for i in range(2, n-2):
    if isPrime(i) and isPrime(n-i):
        print(i,n-i)
        break
    
