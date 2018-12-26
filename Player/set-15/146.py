def factb(a,b):
    if a<=b:
        return 1
    return a*(factb(a-1,b))
            
a,b = map(int,input().split())
print(factb(a,b))
