def isomorphic(s1,s2):
    diff = [-26]*26
    if len(s1)!=len(s2):
        return "no"
    for i in range(len(s1)):
        a = ord(s1[i])
        b = ord(s2[i])
        position = a-97
        new_diff = a-b
        if diff[position]==-26:
            diff[position]=new_diff
        elif diff[position]!=new_diff:
            return "no"
    return "yes"

s1,s2 = input().split()
print(isomorphic(s1,s2))
