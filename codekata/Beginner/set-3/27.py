n = input()
flag = True
string = False
for i in n:
    if i.isdigit():
        pass
    elif i=='.' and flag:
        flag = False
    else:
        string = True
        break

if string:
    print("No")
else:
    print("Yes")
    
