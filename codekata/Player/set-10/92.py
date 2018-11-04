def bcd(n):
    if n==1 or n==0:
        return n
    return n%10+2*(bcd(n//10))

print(bcd(int(input())))
