s = input()
possible = False

for i in range(1,len(s)):
    if s[-i] > s[-i-1]:
        possible = True
        s2 = list(s)
        s2[-i], s2[-i-1] = s2[-i-1], s2[-i]
        break

if possible:
    print("".join(s2))
else:
    print(-1)
