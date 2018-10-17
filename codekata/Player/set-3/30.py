def diffK(str1,str2,k):
    count= 0
    for i in range(len(str1)):
        if count==k:
            return "no"
        if str1[i]!=str2[i]:
            count-=1
    return "yes"

str1,str2,k = input().split()
print(diffK(str1,str2,int(k)))

