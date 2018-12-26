def CheckDigitAndAlphabet(s):
    digitFlag = False
    alphaFlag = False
    for i in s:
        if i.isdigit():
            digitFlag = True
        elif i.isalpha():
            alphaFlag = True
        if digitFlag and alphaFlag:
            return 'Yes'
    return 'No'

s = input()
print(CheckDigitAndAlphabet(s))
