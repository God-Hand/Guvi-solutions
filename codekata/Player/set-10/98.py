n,k = map(int,input().split())
while n>0:
    if n%10>k :
        print('no')
        break
    n = n//10
else:
    print('yes')
