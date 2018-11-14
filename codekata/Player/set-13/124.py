def gcd(a,b):
    if a==b:
        return a
    if a>b:
        return gcd(a-b,b)
    return gcd(a,b-a)
def LCM(a,b):
    return a*b//gcd(a,b)
    
n = int(input())
l = list(map(int,input().split()))
lcm = 1
for i in l:
    lcm = LCM(lcm,i)
print(lcm)
