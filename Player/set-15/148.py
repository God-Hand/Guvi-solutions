n,m = map(int,input().split())
flag = True
for i in range(n):
    nodes, edges = map(int,input().split())
    if edges>=m:
        flag = False
        break;
if flag:
    print("yes")
else:
    print("no")
