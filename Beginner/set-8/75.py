import math
s = input()
l = len(s)

if l%2:
    print(s[:l//2] + '*' +s[l//2+1:])
else:
    print(s[:l//2-1] + '**' +s[l//2+1:])
