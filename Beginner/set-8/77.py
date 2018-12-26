def printFactors(n):
    for i in range(1,n+1):
        if not(n%i):
            print(i,end=" ")

print(printFactors(int(input())))
