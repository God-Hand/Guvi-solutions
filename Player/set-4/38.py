n = int(input())
print(*list(filter(lambda x: not(n%x),[i for i in range(2,n+1,2)])))
