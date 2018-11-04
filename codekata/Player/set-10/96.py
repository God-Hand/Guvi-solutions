n = int(input())
s = n%10
n //= 10
while n>9:
    x = n%10
    n = n//10
print(s+n)
