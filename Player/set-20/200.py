s = input()
l = [False]*(26)
for i in s:
    if l[ord(i)-97]==False:
        l[ord(i)-97]=True
        print(i,end="")
