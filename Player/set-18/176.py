n = set(input())
n2 = set(input())
if len(n.union(n2))==len(n):
    print("true")
else:
    print("false")
