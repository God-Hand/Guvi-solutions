def digitCount(n):
    if n<=9:
        return 1
    return 1 + digitCount(n//10)

def posMul(n, power):
    if n <= 9:
        return n**power
    return (n%10)**power + posMul(n//10, power)

n = int(input())
print(posMul(n, digitCount(n)))
