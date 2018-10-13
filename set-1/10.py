def numberOfDigit(n):
    if n==1:
        return 1
    return n%10+numberOfDigit(n//10)

n = int(input())
print(numberOfDigit(n))
