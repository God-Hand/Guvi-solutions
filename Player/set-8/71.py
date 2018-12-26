n = int(input())
l = list(map(int,input().split()))

previous = l[0]

for i in l[1:]:
    if previous+1 == i:
        print(i, end=' ')
    elif previous-1 == i:
        print(previous, end=' ')
    previous = i
