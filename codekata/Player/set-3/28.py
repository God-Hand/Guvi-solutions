def removeSpaces(n):
    if n!=' ':
        return n
print("".join(list(filter(removeSpaces,input()))))
