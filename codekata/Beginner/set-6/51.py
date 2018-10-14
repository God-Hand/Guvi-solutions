def printDigits(n):
    if n<=9:
        print(n,end=' ')
        return
    printDigits(n//10)
    print(n%10,end=' ')

n = int(input())
printDigits(n)
