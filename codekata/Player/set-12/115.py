s1,s2 = input().split()
if s1>s2:
    print(s1[:len(s2)] + s2)
else:
    print(s1 + s2[:len(s1)])
