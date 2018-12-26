n = list(input().split())
n2 = list(input().split())
for i in n:
    if i not in n2:
        print(i,end=" ")
for i in n2:
    if i not in n:
        print(i,end=" ")
