import math as m
n = input()
p = len(n)

sum=0
for i in n:
    sum+=m.pow(int(i),p)

if sum==int(n):
    print("yes")
else:
    print("no")
