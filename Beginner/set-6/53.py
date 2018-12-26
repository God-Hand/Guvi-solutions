def getSum(n):
    if n<=9:
        return n
    return n%10 + getSum(n//10)

print(getSum(int(input())))
