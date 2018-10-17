s = input()
d = dict([])
max_char = 'a'
max_value = 1
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

    if d[i] > max_value:
        max_value = d[i]
        max_char = i

print(max_char)
