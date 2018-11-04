n = int(input())
l = []
while n>0:
    x = n%10
    n = n//10
    if x not in l:
        l.append(x)
    else:
        print('yes')
        break
else:
    print('no')
