s,k = input().split()
k = int(k)%len(s)
print(s[k:]+s[:k])
