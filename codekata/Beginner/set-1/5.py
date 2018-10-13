a,b,c = map(int,input().split())
max = a if a>b else b
max = c if max<c else max
print(max)
