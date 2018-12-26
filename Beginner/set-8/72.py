def haveVowel():
    for i in s:
        if i in 'aeiou':
            return "yes"
    return "no"
print(haveVowel(input()))
