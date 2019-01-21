def palindromic_length( center, diff, string):
    if center-diff == -1 or center+diff == len(string) or string[center-diff] != string[center+diff] :
        return 0
    return 1 + palindromic_length(center, diff+1, string)

def palindromic_string( input_string ):
    max_length = 0    
    new_input_string = ""

    for i in input_string[:len(input_string)-1] :
        new_input_string += i + "|"
    new_input_string += input_string[-1]

    for i in range(len(new_input_string)) :
        length = palindromic_length(i, 1, new_input_string)

        if max_length < length :
            max_length = length
            start = i
    
    return max_length


if __name__ == '__main__':
    n = input()
    print(palindromic_string(n))
