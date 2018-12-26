n,k = map(int,input().split())
count = 0
for _ in range(n):
    s = input()
    flag = False
    for i in ('a','e','i','o','u'):
        if i in s:
            flag = True
            break
    if flag:
        count+=1
if count>=k:
    print("yes")
else:
    print("no")
