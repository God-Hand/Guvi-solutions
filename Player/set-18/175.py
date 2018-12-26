n = set(input())
n2 = set(input())
if len(n.union(n2))==26:
    print("complementary")
else:
    print("non-complementary")
