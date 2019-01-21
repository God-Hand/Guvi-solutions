def posMul(n, count):
    if n <= 9:
        return count*n
    return count*(n%10) + posMul(n//10, count+1)

print(posMul(int(input()), 1))
