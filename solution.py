def getCount(inputStr):
    num_vowels = 0
    print(inputStr)
    
    for i in inputStr:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            num_vowels += 1

    return num_vowels
