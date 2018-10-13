import re
s = input()
count=0
for i in s:
    if i.isdigit():
        count+=1
print(count)
