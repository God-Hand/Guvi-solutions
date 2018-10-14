def getKCount(l,k):
    kCount = 0
    for i in l:
        if i==k:
            kCount+=1

    return kCount

n,k = map(int, input().split())
l = list(map(int, input().split()))
print(getKCount(l,k))
