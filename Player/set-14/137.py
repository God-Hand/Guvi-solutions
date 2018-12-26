def d2b(n):
    if n==0 or n==1:
        return str(n)
    return str(n%2) + d2b(n//2)
b = d2b(int(input()))
for i in range(len(b)):
    if b[i]=='1':
        print(i+1)
        break
if b=='0':
    print(0)
