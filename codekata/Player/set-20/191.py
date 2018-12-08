n = int(input())
l = list(map(int,input().split()))
l2 = list(map(int,input().split()))

if set(l)==set(l2):
    print("yes")
else:
    print("no")
