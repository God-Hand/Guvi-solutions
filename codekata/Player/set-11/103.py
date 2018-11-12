n = int(input())
l = sorted(list(map(int,input().split())),reverse=True)
ml = l[:n//2]
print(sum(ml)*(n-1)//(n//2))
