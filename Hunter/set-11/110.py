import re
n = int(input())
l = list(input().split())

for x in l:
    if x == "1" or x == "4" or x == "78":
        print("+")
    elif "5" == x[-1] and x[-2] == "3":
        print("-")
    elif x[0] == "1" and x[1] == "9" and x[2] == "0":
        print("?")
    else:
        print("*")
