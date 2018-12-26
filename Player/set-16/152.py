s = input()
vowels = 0
constants = 0
for i in s:
    if i in ['a','e','i','o','u']:
        vowels+=1
    else:
        constants += 1
if vowels>constants:
    print(2*constants+1)
elif constants>vowels :
    print(2*constants+1)
else:
    print(2*constants)
