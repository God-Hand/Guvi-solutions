import re
s = input()
count=1
for i in s:
    if i=='.':
        count+=1
print(count)
