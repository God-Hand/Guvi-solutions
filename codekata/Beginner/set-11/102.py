n = int(input())
while True:
    if n//2*2 == n:
        n//=2
    else:
        break
print(n)
