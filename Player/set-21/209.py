n = int(input())
d1 = 1
d2 = 1
for i in range(n):
	l = list(map(int,input().split()))
	for j in range(n):
		if i==j:
			d1 *= l[j]
		if i+j = n-1:
			d2 *= l[j]
print(d1*d2)