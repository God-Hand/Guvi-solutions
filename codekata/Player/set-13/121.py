def countBits(n):
    if not n:
        return 0
    else:
        return 1 + countBits(n//2)
print(countBits(int(input())))
