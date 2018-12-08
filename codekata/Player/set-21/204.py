n = int(input())
l = list(map(int,input().split()))
print(sum(list(filter(lambda x:x<0,l))))
