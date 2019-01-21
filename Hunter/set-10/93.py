s = input()
s2 = list(s)
odd = True
for i in range(len(s)):
    if odd and s[i] not in " !@#$'":
        odd = False
        s2[i] = s[i].upper()
    else:
        odd = True

print("".join(s2))
