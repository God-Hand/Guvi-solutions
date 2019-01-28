import sys

def minCoinsCount(coins, cost):
    dp = [0] * (cost+1)

    dp[0] = 0
    for i in range(1,cost+1):
        dp[i] = sys.maxsize

    for i in range(1, cost+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                sub_res = dp[i-coins[j]]
                if sub_res != sys.maxsize and sub_res + 1 < dp[i]:
                    dp[i] = sub_res +1

    if dp[cost] == sys.maxsize:
        return -1
    return dp[cost]

n,k = map(int,input().split())
coins = list(map(int,input().split()))
print(minCoinsCount(coins, k))
