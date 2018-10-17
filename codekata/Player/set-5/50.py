import math
def isPrimeNot(n):
    for i in range(2,int(math.sqrt(n))+1):
        if not n%i:
            return "yes"
    return "no"

print(isPrimeNot(int(input())))
