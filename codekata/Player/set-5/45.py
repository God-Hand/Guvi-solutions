import math
p,a = map(int,input().split())
r1 = (p + int(math.sqrt(p**2 - 16*a)))//(4)
r2 = (p - int(math.sqrt(p**2 - 16*a)))//(4)
if 2*(r1+r2)==p and r1*r2==a:
    print('yes')
else:
    print('no')
