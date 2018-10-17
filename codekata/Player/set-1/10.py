def diffOne(s1,s2):
    diff = 2
    for i in range(len(s1)):
        if s1[i]!=s2[i] and diff:
            diff-=1
        if not diff:
            return "no"
    return "yes"

s1, s2 = list(input().split())
print(diffOne(s1,s2))
