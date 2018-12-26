def is_perfect_square(n):
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y:
            return "no"
        y.add(x)
    return "yes"
a,b = map(int,input().split())
print(is_perfect_square(a*b))
