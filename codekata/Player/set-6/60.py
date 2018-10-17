s1,s2 = input().split()
for i in range(len(s1)):
    if s1[i]==s2[i]:
        print("yes")
        break
else:
    print("no")
