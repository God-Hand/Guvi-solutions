def coPrimes(a,b):
    if a%b==0 and b!=1:
        return False
    else:
        if a==1 or b==1:
            return True
        else:
            return coPrimes(b,a%b)

a,b = input().split()
if coPrimes(len(a),len(b)):
    print("yes")
else:
    print("no")
