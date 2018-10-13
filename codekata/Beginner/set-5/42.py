# trying to make it as c comparing
s1, s2 = input().split()
l1 = len(s1)
l2 = len(s2)
equal = True
for i in range(len(max(l1,l2))):
    if s1[i]>s2[i]:
        print(s1)
        equal = False
        break
    elif s1[i]<s2[i]:
        print(s2)
        equal = False
        break

if equal:
    print(s1)
