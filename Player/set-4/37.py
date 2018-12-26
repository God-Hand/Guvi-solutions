d1 = {}
d2 = {}
for i in range(int(input())):
    x,y = map(int,input().split())
    d1[x]=y
    d2[y]=x
print(min(len(d1),len(d2))-1)
