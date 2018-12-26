def countOccurance(s,k):
    count = 0
    for i in range(len(s)):
        if s[i]==k:
            count+=1
    return count

s,k = input().split()
print(countOccurance(s,k))
