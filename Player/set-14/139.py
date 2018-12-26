def count1(n):
    if n==0:
        return 0
    return n%2 + count1(n//2)
print(count1(int(input())))
