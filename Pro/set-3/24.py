def printCombinations(k):
    dp =[[] for i in range(k+1)]
    dp[0].append('')
    
    for i in range(1,k+1):
        d = dp
        dp =[[] for i in range(k+1)]
        dp[0].append("0"*i)
        for j in range(1,i+1):
            for s in d[j]:
                dp[j].append("0"+s)
            for s in d[j-1]:
                dp[j].append("1"+s)

    for i in dp:
        print(*i,sep="\n")
printCombinations(int(input()))
