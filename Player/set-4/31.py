l = list(input())
count = 0
if len(l)%2:
    print("no")
elif l[0]==')' or l[-1]=='(':
    print("no")
else:
    for i in range(len(l)):
        if l[i]=='(':
            count+=1
        else:
            count-=1
    if count:
        print("no")
    else:
        print("yes")

