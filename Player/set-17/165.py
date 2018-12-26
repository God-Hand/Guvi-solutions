n,k = map(int,input().split())
kl = list(map(int,input().split()))
found = 100000
for i in kl:
    if i>k and i<found:
        found = i
print(found)
