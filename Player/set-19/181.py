def isSum(n,a,b):
    if a<b:
        b,a=a,b
    while n>=0:
        if n%a==0:
            return True
        n-=b
    return False
        
n = int(input())
if isSum(n,3,7):
    print("yes")
else:
    print("no")
