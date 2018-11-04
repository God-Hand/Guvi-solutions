def bch(n):
    if n==1 or n==0:
        return n
    s = 0
    for i in range(4):
        s += (2**i)*(n%10)
        n = n//10
    return s + 10*bch(n)
    
print(bch(int(input())))
