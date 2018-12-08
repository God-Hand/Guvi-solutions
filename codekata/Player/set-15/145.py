n = int(input())
l = list(map(int,input().split()))
mult = 1
for i in l:
    mult*=i
if mult==n:
    print("yes")
else:
    print("no")
