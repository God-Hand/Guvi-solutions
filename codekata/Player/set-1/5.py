import functools
def value(r):
    if (r == 'I'): 
        return 1
    if (r == 'V'): 
        return 5
    if (r == 'X'): 
        return 10
    if (r == 'L'): 
        return 50
    if (r == 'C'): 
        return 100
    if (r == 'D'): 
        return 500
    if (r == 'M'): 
        return 1000

def romanToInt(x,y):
    a = value(x)
    b = value(y)
    if a>b:
        return a+b
    else:
        return b-a
    
a = functools.reduce(romanToInt,input())
print(a)
