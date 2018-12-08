import math
def isprime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if not n%i:
            return False
    return True
if isprime(len(input())):
    print("yes")
else:
    print("no")
