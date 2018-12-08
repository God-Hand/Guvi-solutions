def canWe(l):
    count=0
    n = len(l)
    for i in range(n//2):
        if l[i]!=l[-i-1]:
            count+=1
        if count>1:
            return "no"
    return "yes"
print(canWe(input()))
