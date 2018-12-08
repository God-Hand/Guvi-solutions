n = int(input())
l = []
for i in range(n):
    l.append(input())
print(*sorted(l),sep="\n")
