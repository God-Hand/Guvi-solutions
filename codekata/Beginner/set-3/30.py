h1,m1 = map(int,input().split())
h2,m2 = map(int,input().split())

if m2>m1:
    m1+=60
    h1-=1

print(h1-h2, m1-m2)
