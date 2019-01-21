def gcd(n,m):
    if m == 0:
        return n
    return gcd(m, n%m)

n,m = map(int,input().split())
if gcd(n,m)==1:
    print("yes")
else:
    print("no")
