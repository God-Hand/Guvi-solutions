n,k = map(int,input().split())
kl = list(map(int,input().split()))
found = 0
for i in kl:
    if i<=k and i>found:
        found = i
print(found)
