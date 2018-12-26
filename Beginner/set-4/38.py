def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a,b
x, y = map(int,input().split())
print(*swap(x,y))
