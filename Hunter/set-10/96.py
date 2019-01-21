def num(n):
    if n<9:
        return n
    return 9 + 10*num(n-9)
    
n = int(input())
print(num(n))
