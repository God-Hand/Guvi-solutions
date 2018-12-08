n,m = map(int,input().split())
flag = True
for i in range(n):
    nodes, edges = map(int,input().split())
    if edges>=m:
        flag = False
        break;
if flag:
    print("no")
else:
    print("yes")
