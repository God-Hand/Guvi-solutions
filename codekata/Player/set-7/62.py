n = int(input())
min = 1
while min<n:
    if (n//min)%2 != 0 and n%min==0:
        break
    min += 1
print(min)
