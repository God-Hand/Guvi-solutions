def isPerfectSquare(n):
    x = n//2
    l = [x]
    while x*x!=n:
        x=(x+n//x)//2
        if x in l:
            return False
        l.append(x)
    return True

l,r = map(int,input().split())
print(len(list(filter(isPerfectSquare,range(l,r+1)))))
