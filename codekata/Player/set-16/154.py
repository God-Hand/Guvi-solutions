s,k = input().split()
k = int(k)
newS = ''
for i in range(len(s)):
    if not (i+1)%k:
        newS += s[i].upper()
    else:
        newS += s[i]
print(newS)
