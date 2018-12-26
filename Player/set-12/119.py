switcher = {'A':10,'B':11,'C':12,'D':13,'E':15,'F':16}
def htod(n):
    if len(n)==0:
        return 0
    if n[0] in switcher:
        return switcher[n[0]] + htod(n[1:])
    else:
        return int(n) + htod(n[1:])

n = input()
print(htod(n))
