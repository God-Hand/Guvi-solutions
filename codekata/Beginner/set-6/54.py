def getNearEven(n):
    if n%2:
        return n-1
    else:
        return n

print(getNearEven(int(input())))
