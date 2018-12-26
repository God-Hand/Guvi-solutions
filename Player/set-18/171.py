s = list(input().split())
for i in range(1,len(s)-1):
    if s[i] == "and":
        s[i-1],s[i+1] = s[i+1],s[i-1]
print(*s)
