def isPresent(l,k):
    for i in l:
        if i==k:
            return 'yes'
    return 'no'

n,k = map(int, input().split())
l = list(map(int, input().split()))
print(isPresent(l,k))
