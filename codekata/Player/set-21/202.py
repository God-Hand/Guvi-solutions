s = input()
v=''
c=''
for i in s:
    if i in ('a','e','i','o','u'):
        c+=i
    else:
        v+=i
print(c+v)
