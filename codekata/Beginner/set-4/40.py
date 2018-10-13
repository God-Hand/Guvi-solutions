n = int(input())
if n==1:
    print(1)
elif n==2:
    print(1,1)
else:
    a = 1
    b = 1
    print(1,1,end=' ')
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c,end=' ')
