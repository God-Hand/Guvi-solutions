n,k = map(int,input().split())
if n%2 == 0:
    n+=1
s = 0
for i in range(n,k,2):
    s+=i
print(s)
