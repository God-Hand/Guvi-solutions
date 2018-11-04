n = int(input()])
l = sorted(list(map(int,input().split())))

for i in l:
    if i < n:
        print(i,end=' ')
