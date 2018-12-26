l = []
for i in range(int(input())):
    l.append(input())
previous = l[0]
flag = False
for i in l[1:]:
    l = list(previous)
    for j in i:
        if j in l:
            flag = True
            break
    if flag == True:
        break
    previous = i
if flag:
    print('yes')
else:
    print('no')
