flag = False
for _ in range(int(input())):
    s = input()
    flag = False
    for i in ('a','e','i','o','u'):
        if i in s:
            flag = True
            break
    if not flag:
        break
if flag:
    print("yes")
else:
    print("no")
