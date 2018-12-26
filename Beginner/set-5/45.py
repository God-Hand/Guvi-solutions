def countDigit(n):
    if n<=9:
        return 1
    return 1+countDigit(n//10)

print(countDigit(int(input())))
