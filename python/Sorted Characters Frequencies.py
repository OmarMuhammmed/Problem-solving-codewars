def sorted_char_frequencies(string):
    dict = {}
    
    
    for char in string.lower():
        if char ==" ":
            continue
        if char in dict.keys():
            dict[char] += 1
        else:
            dict[char] = 1 

    return dict


sorted_char_frequencies('hello, world')
print(sorted_char_frequencies('hello, world'))
