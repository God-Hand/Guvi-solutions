import re
s = input()
count=0
for i in s:
    if not(i.isalnum()):
        count+=1
print(count)
