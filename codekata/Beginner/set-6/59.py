def getDigitCount(n):
    if n<=9:
        return 1
    return 1 + getDigitCount(n//10)

print(getDigitCount(int(input())))

