from math import sqrt
def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if not n%i:
            return False
    return True

def printAll(n):
    if 2<n:
        print(2,end=" ")
    for i in range(3, n, 2):
        if isPrime(i):
            print(i, end=" ")

printAll(int(input()))
