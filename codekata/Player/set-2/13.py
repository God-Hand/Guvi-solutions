def sumDigitSquare(n):
    if n<=9:
        return n**2
    return (n%10)**2 + sumDigitSquare(n//10)

print(sumDigitSquare(int(input())))
