def checkProduct(n,m):
    if (n*m)%2:
        return "odd"
    else:
        return "even"

n,m = map(int, input().split())
print(checkProduct(n,m))
