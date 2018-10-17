def countOccurance(s,k):
    print(s)
    count = 0
    for i in s:
        if i==k:
            count+=1
    return count

sentense = input()
word = input()
print(countOccurance(sentense,word))
