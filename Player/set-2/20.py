def add3(n):
    x = (ord(n)-62)%26
    return chr(x+65)

print("".join(list(map(add3,input()))))
