import math as m
def isPrime(n):
    for i in range(2,int(m.sqrt(n))+1):
        if not(n%i):
            return 'no'
    return 'yes'
print(isPrime(int(input())))

