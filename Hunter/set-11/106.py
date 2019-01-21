a = input()
b = input()

x = min(len(a), len(b))
for i in range(x):
    print(b[i]+a[i])

for i in range(x, len(a)):
    print(a[i])

for i in range(x, len(b)):
    print(b[i])
