def isnum(i):
    if i.isnumeric():
        return True
    return False

s = input()
print("".join(filter(isnum, s)))
