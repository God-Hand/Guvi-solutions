import math as m
def digitSum(x):
  if x<=9:
    return x
  return x%10 + digitSum(x//10)

def printPossibleWays(n):
  start = n - min(n,9*m.ceil(m.log10(n)))
  l = []
  for i in range(start, n):
    if i+digitSum(i) == n:
      l.append(i)

  if len(l):
    print(len(l))
    print(*l, sep="\n")
  else:
    print("-1")


printPossibleWays(int(input()))
