def bco(n):
    if n==1 or n==0:
        return n
    s = 0
    for i in range(3):
        s += (2**i)*(n%10)
        n = n//10
    return s + 10*bco(n)
    
print(bco(int(input())))
