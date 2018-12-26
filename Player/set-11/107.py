s = input()
x = input()

for i in range(len(s)):
    if s[i] == x[0]:
        j = 1
        while j<len(x):
            if s[i+j] == x[j]:
                j+=1
            else:
                break
        if j==len(x):
            print(i+1)
            break
