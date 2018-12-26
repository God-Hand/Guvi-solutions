l = list(input().split())
min = l[0]
for x in l[1:]:
    if min < x:
        x = min

print(min)
