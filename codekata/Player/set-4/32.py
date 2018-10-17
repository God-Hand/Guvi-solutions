n,k = map(int,input().split())
li = list(map(int,input().split()))

def binary_search(li,l,r,x):
    if r>l:
        mid = (r+l-1)//2
        if li[mid]==x:
            return "yes"
        elif li[mid]<x:
            return binary_search(li,mid+1,r,x)
        else:
            return binary_search(li,l,mid-1,x)
    return "no"

print(binary_search(li,0,n-1,k))
