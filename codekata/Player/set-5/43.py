def isSubStr(str1, str2):
    s2 = len(str2)
    for i in range(len(str1)-len(str2)):
        if str1[i:s2+i]==str2:
            return "yes"
    return "no"

str1, str2 = input().split()
print(isSubStr(str1,str2))
