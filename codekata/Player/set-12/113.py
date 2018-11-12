import re
n = input()
if re.match('^(0\d|[12]\d|3[01])/(0[1-9]|1[012])/(19|20)\d\d$',n):
    print(n)
else:
    print('no')
