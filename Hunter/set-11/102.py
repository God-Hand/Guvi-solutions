l = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def digitSquare(n):
    if n <= 9:
        return l[n]
    return l[n%10] + digitSquare(n//10)

print(digitSquare(int(input())))
