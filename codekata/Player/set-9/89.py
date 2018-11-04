def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)
n,r = map(int,input().split())
print(fac(n)//fac(n-r))
