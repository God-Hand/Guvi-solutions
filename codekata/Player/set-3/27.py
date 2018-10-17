def changeCase(n):
    x = ord(n)
    if x>=65 and x<=90:
        return chr(x+32)
    else:
        return chr(x-32)
print("".join(list(map(changeCase,input()))))
