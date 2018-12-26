def reverseN(n):
    if not n//10:
        return str(n)
    return str(n%10) + reverseN(n//10)

print(reverseN(int(input())))
