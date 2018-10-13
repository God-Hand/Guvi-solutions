def swap(x,y):
    return y,x
x,y = map(int,input().split())
print(*swap(x,y))
