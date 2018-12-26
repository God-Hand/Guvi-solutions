n,k = map(int,input().split())
s = input()
l = sorted(list(map(int,input().split())),reverse=True)
kl = list(map(int,input().split()))
for i in kl:
    l.append(i)
    print(sorted(l,reverse=True)[0],end=" ")
