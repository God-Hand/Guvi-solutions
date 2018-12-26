n = int(input())
l = list(map(int,input().split()))
presum = 0
for i in l:
    presum += i
    if i%2:
        print(i,end=' ')
    else:
        print(presum, end=' ')
