def isNum(n):
    for i in n:
        if ord(i)<48 or ord(i)>57:
            return "no"
    return "yes"

print(isNum(input()))
