def digitSum(n):
    if n == 0:
        return 0
    if n%2:
        return n%10 + digitSum(n//10)
    else:
        return digitSum(n//10)
if digitSum(int(input()))%2:
    print('O')
else:
    print('E')
