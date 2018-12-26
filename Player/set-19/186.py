import re
s = input()
if re.search('Vishal',s) and re.search('Sundar',s):
    print("yes")
else:
    print("no")
