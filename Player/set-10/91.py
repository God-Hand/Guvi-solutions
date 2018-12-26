def dcb(n):
    if n==1 or n==0:
        return n
    return n%2+10*(dcb(n//2))

print(dcb(int(input())))
