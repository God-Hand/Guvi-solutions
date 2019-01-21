l = list(input().split())
for i in range(len(l)):
    l[i] = l[i].lower()

l = sorted(l)
print(*l, sep="\n")
