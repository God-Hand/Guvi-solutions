s = input()
count = 1
previous = s[1]
for i in range(1,len(s)):
    if s[i] == previous:
        count+=1
    else:
        print(previous+str(count),end='')
        previous = s[i]
        count=1
print(previous+str(count))
