x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

if x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2):
    print("no")
else:
    print("yes")
