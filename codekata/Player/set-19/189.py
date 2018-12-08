a,b,c = map(int,input().split())
if (a+b>c or b+c>a or c+a>b) and (a!=b and b!=c):
    print("yes")
else:
    print("no")
