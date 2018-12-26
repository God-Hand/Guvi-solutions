s,k = input().split()
def firstPosition(s,k):
    for i in range(len(s)):
        if s[i]==k:
            return i+1
    return "yes"

print(firstPosition(s,k))
