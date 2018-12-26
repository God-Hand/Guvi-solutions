import math as m
def isprime(n):
    for i in range(2, int(m.sqrt(n)+1)):
        if not n%i:
            return False
    return True
for i in range(2,int(input())):
    if isprime(i):
        print(i,end=' ')
