f = 1
def posMul(n, p):
    if n <= 9:
        f = n
        return n**p
    return (n%10)**p + posMul(n//10, n%10)

n = int(input())
print(posMul(n, 0) - 1 + (n%10)**f)
