def isAlternating(n,l):
    state = 'I'
    for i in range(1,n):
        if l[i] > l[i-1] and state=='D':
            return "no"
        if l[i] < l[i-1] and state=='I':
            return "no"
        if state=='I':
            state='D'
        else:
            state='I'
    return "yes"
    
n = int(input())
l = list(map(int,input().split()))
print(isAlternating(n,l))
