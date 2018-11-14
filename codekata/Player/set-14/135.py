n = int(input())
l = list(map(int,input().split()))
print(*sorted(l[:n//2]),*sorted(l[n//2:],reverse=True))
