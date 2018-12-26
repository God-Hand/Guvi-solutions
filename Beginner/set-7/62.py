s = input()
for i in range(len(s)):
    if s[i]!=0 and s[i]!=1:
        break
if i==len(s)-1:
    print("yes")
else:
    print("no")
