from collections import Counter
s = input()
print("Yes" if sorted(Counter(s).values())[-1]==1 else "No")
