n = int(input())
l = map(int,input().split())

even = 0
odd = 1
evencount = 0

for i in l:
    if i%2:
        odd = i
    else:
        even = i
        evencount += 1
if evencount == 1:
    print(even)
else:
    print(odd)
