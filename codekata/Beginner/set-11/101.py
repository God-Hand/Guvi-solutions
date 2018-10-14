import functools
l = list(map(int,input()))
print(functools.reduce(lambda a,b:a*b ,l))
