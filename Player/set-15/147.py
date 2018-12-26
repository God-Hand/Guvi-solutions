a,b,c = map(int,input().split())
mult = 1
for i in range(b):
    if mult%c==0:
        mult*=a
    else:
        mult = (mult%c) * a

print(mult%c)
