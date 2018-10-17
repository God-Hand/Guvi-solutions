s1,s2 = input().split()
def sameOrNot(s1,s2):
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            return "no"
    return "yes"

print(sameOrNot(s1,s2))
