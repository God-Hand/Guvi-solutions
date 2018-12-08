n = int(input())
l = list(map(int,input().split()))
print(len(list(filter(lambda x:x<0,l))))
